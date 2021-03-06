# -*- coding:utf8 -*-
from __future__ import with_statement
from fabric.api import run
from fabric.api import local
import logging
from fabric.api import local, settings, abort, lcd, cd, get, env, roles, task, hide,sudo
from fabric.contrib.console import confirm


def linux_type():
    """
        判断系统的类型
        ubuntu or centos
        :return:
    """
    pass


def is_ubuntu():
    os = run('cat /etc/issue')
    return os.lower().find('ubuntu') >= 0


def is_centos():
    os = run('cat /etc/issue')
    return os.lower().find('centos') >= 0


def has_user(username):
    res = run('cat /etc/passwd | grep %s | wc -l' % username)
    return res != '0'


def install_packages(package=[], runner=sudo):
    if is_ubuntu():
        runner('apt -y install %s' % ' '.join(package))
    elif is_centos():
        runner('yum -y install %s' % ' '.join(package))


def linux_version():
    """
        判断系统的版本
        :return:
    """
    pass