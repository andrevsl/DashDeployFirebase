"""
main script for Dash application
"""

import dash_core_components as dcc
import dash_html_components as html
import requests

import dash
from create_jwt_from_sa import generate_jwt
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# url for Cloud engpoint
endpoint_url = "https://flaskapp-cr-v2-gateway-yerjarnciq-ue.a.run.app"

# Paramters for JWT
sa_keyfile = # $MY_CREDENTIAL_JSON_FILE
sa_email = # $MY_SERVICE_ACCOUNT_ADDRESS
expire = 300  # you can set some integer
aud = # $AUD_URL

# The dash
app = dash.Dash(__name__)

# Design for Dash
app.layout = html.Div(
    [
        html.Div(id="default_div", children="Please enter your name"),
        html.Div(dcc.Input(id="message_input", type="text")),
        html.Button("Submit to API!", id="submit_button", n_clicks=0),
        html.Div(id="message_div", children=""),
    ]
)


@app.callback(
    Output("message_div", "children"),
    [Input("submit_button", "n_clicks")],
    [State("message_input", "value")],
)
def press_submit_button(n_clicks, value):
    # If the is no input is given in message_div (box), no updates
    if not value:
        raise PreventUpdate

    # Create JWT
    jwt = generate_jwt(sa_keyfile, sa_email, expire, aud)
    # Header for Autheorizarion (Checked by Cloud Endpoint)
    auth_header = {"Authorization": f"Bearer {jwt}"}

    # Create a request
    resp = requests.post(
        f"{endpoint_url}/hello_body",
        data={"my_name": f"{value}"},
        verify=False,
        headers=auth_header,
    )
    resp_message = resp.content.decode()
    return f"Response from Cloud Run: {resp_message}"


if __name__ == "__main__":
    app.run_server(debug=True)