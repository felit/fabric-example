from ssh import fabfile2
from fabric.api import run, env, execute, roles, runs_once, parallel, sudo, hosts, cd, task
# env.hosts = ['vagrant@192.168.36.10']
env.hosts = ['vagrant@192.168.58.10', 'vagrant@192.168.58.12', 'vagrant@192.168.58.13']
# env.passwords={
# 'vagrant@192.168.58.10':'vagrant',
# 'vagrant@192.168.58.12':'vagrant',
#     'vagrant@192.168.58.13':'vagrant'
# }
# TODO password
env.roledefs = {'master': env.hosts[0:1]}


@task
@runs_once
def add_keys():
    local_key = """ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDHJXAZx0EzfFtyoFJvimiP1J4/XZZU7WOtx/cH2/dHAi5eBjqk5WjSRVgYGmJWCrivE2KEub25fGqR1wVnZXSfP3x9PsQnE5eO5I/K2OAfUGakHVZeYKm3J5ADryxcRxcKj8d0Y+/PHSyrL0smN+ZyyYqFJ2nfW2tGYKAK9bwdwjcf/QgnR558SbWAjKmBp81JUxQUpkNO+Hv4yIaPPbsYXsVk752DjIrgsE2riGrjCLju1yBu6T7mYw0wEpn4XrE0WQfyZkBRV/BS4Iz1iFYQExrsWaJbe82Gt00TJksbJJN81FGtllmo1AdGTVonwpv3dAS6AMfT2RcFrPZw018v congsl@congsl"""
    vagrant_key = """ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCitSbjuskzFXwoIkGw3SVbjxQdoIZBlfuUH6unPdHc7411zj60db/kOKzJPNArvsbSizEt3BuPe+NmrvLyYlHleBYlG1Eo2a1r/H3SX4ss0jvVU8M4fzyASu/wUoX6L5dtOlS6Ja4sL32UAN98nXv6gyNAkEafEJ+yZl/GYkjJpJq9HSpV4bW49w6qcp28nlyxfMJLZj23cuxjTLUreySlnjECRGn5Xi7ynxqo60WnSqOdlLHD6pR6JfaOXtIg+tB0F88yKsAtSqH/G9bN3j3vxms3eFD5UJzESfjBXLJ6i40Lk6QNg+rJjYwAGDPrgCmfncwYqKaWfzs7WO0Imker vagrant"""
    execute(fabfile2.add_public_key_authorizied_keys, add_keys=[local_key, vagrant_key])