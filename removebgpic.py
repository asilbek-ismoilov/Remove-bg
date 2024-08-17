import requests

def remove_bg_pic(FILE_NAME): 
    rasm=''
    API_KEY = 'C2oZstkzowzVkEisgZ1cMg5q'

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        data={
            'image_url': FILE_NAME,
            'size': 'auto'
        },
        files={},
        headers={'X-Api-Key': API_KEY})
    
    if response.status_code == requests.codes.ok:
        rasm = response.content
    else:
        print("Error:", response.status_code, response.text)
    
    return rasm
