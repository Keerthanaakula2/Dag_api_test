import smtplib
from google.cloud import secretmanager

def send_email(request):
    # Initialize the Secret Manager client
    client = secretmanager.SecretManagerServiceClient()

    # Replace with your project ID and secret names
    project_id = 'keerthanacicd'
    secret_username = 'projects/{}/secrets/tech_projects/versions/latest'.format(project_id)
    secret_password = 'projects/{}/secrets/Impetus123/versions/latest'.format(project_id)

    # Retrieve secret values
    username = client.access_secret_version(request={"name": secret_username}).payload.data.decode("UTF-8")
    password = client.access_secret_version(request={"name": secret_password}).payload.data.decode("UTF-8")

    recipient_email = 'kakula@cswg.com'
    sender_email = 'techprojectscloud@gmail.com'

    message = """\
    Subject: Build Successful!

    Your Cloud Build tests were successful!
    """

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(sender_email, recipient_email, message)
        return 'Email sent successfully', 200
    except Exception as e:
        return 'Error sending email: ' + str(e), 500
