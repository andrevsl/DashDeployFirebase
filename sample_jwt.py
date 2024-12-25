from DashDeployFirebase.sample_jwt import generate_jwt

sa_keyfile = # $MY_CREDENTIAL_JSON_FILE
sa_email = # $MY_SERVICE_ACCOUNT_ADDRESS
expire = 300  # you can set some integer
aud = # $AUD_URL

jwt = generate_jwt(sa_keyfile, sa_email, expire, aud)