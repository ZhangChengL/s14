#!/bin/bash

echo '================================================================'
echo '===                                                         ===='
echo '===                 Welcome To Use ftxjoy Soft                ===='
echo '===                                V1.0@2016                ===='
echo '===                                                         ===='
echo '================================================================'

echo ' Starting...'


if [ ! -d "/tmp/install" ]; then
    mkdir -p /tmp/install
    \cp -rf * /tmp/install
fi

cd /tmp/install/shell

sh system.sh
