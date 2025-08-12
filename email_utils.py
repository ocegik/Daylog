# email_utils.py
import re
import dns.resolver
import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
from config import EMAIL_ADDRESS, EMAIL_PASSWORD

def is_valid_email_format(email):  # Information can be passed into functions by parameters/arguments
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # determining characters that email will allow
    return re.match(pattern, email) is not None  # it matches pattern with email if they don't match it return nothing

def has_mx_record(email):  # Take email as an argument and uses DNS library
    domain = email.split('@')[1]  # Split email in two parts before and after @, enter 0 to get before @ part
    try:
        records = dns.resolver.resolve(domain, 'MX')
        return bool(records)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return False

def generate_verification_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def send_email_verification(user_email, username, verification_code):
    env = Environment(loader=FileSystemLoader('templates'), autoescape=True)
    template = env.get_template('email_template.html')
    html_content = template.render(username=username, verification_code=verification_code)
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = user_email
    msg['Subject'] = 'Verify Your Email'

    # plain_text = f"Hi {username},\nPlease verify your email by entering this code: {verification_code}"

    msg.attach(MIMEText(html_content, 'html'))
    # msg.attach(MIMEText(plain_text, 'plain'))

    server = smtplib.SMTP('smtp.outlook.com', 587)  # Use your SMTP server details
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(EMAIL_ADDRESS, user_email, text)
    server.quit()