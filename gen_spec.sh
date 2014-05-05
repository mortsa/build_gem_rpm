#! /bin/bash
#
# gen_spec.sh
# Copyright (C) 2014 tim <tim@titanium.co.goldfish>
#
# Distributed under terms of the MIT license.
#


GEM='r10k'
GEM_VERSION=''
TMPDIR=$(mktemp -d)
RETOUT=$(cd ${TMPDIR} && gem fetch ${GEM})
RETVAL=$?
if [ ${RETVAL} -eq 0 ]
then 
    GEM_VERSION=$(echo ${RETOUT}|awk '{print $2}')
    echo "Downloaded: ${GEM_VERSION}"
else 
    echo "Error: ${RETOUT}"
fi
TMPL=rubygem-${GEM}.spec.template
if [ ! -f ${TMPL} ]
then
    gem2rpm -T > ${TMPL}
    echo "Generated new spec template: ${TMPL}"
fi
if [ -f rubygem-${GEM}.spec.template ] 
then
    gem2rpm -t rubygem-${GEM}.spec.template ${TMPDIR}/${GEM_VERSION}.gem > rubygem-${GEM}.spec
fi
[ -d ${TMPDIR} ] && rm -rf ${TMPDIR}

