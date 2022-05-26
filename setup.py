#!/usr/bin/env python3
import os
from setuptools import setup

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

PLUGIN_ENTRY_POINT = 'ovos-PHAL-plugin-wifi-setup=ovos_PHAL_plugin_wifi_setup:WifiSetupPlugin'
setup(
    name='ovos-PHAL-plugin-wifi-setup',
    version='0.0.1',
    description='A plugin for OpenVoiceOS hardware abstraction layer',
    url='https://github.com/OpenVoiceOS/ovos-PHAL-plugin-wifi-setup',
    author='Aiix',
    author_email='aix.m@outlook.com',
    license='Apache-2.0',
    packages=['ovos_PHAL_plugin_wifi_setup'],
    package_data={'': package_files('ovos_PHAL_plugin_wifi_setup')},
    install_requires=["ovos-plugin-manager>=0.0.1"],
    zip_safe=True,
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={'ovos.plugin.phal': PLUGIN_ENTRY_POINT}
)