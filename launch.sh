#!/bin/bash
service network-manager stop &&
/etc/init.d/xencommons start &&
/etc/init.d/xendomains start &&
#/etc/init.d/xen-watchdog start &&
#/etc/init.d/xendriverdomain start &&
ifdown enp6s0 &&
ifup enp6s0 &&
ifup xenbr0
