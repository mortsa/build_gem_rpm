#! /bin/bash
#
# build.sh
# Copyright (C) 2014 tim <tim@titanium.co.goldfish>
#
# Distributed under terms of the MIT license.
#

SPEC=rubygem-r10k.spec
BUILD_DATE=$(date +%Y%m%d%H%M%S)
BUILD_DIR=~/tmp/mock_tmp/
spectool -gf --sourcedir ${SPEC}
mock -r epel-6-x86_64 --buildsrpm --spec=${SPEC} --sources ~/rpmbuild/SOURCES/
mkdir -p ${BUILD_DIR}/${SPEC}/${BUILD_DATE}
rsync -av /var/lib/mock/epel-6-x86_64/result/ ${BUILD_DIR}/${SPEC}/${BUILD_DATE}/
for SRPM in ${BUILD_DIR}/${SPEC}/${BUILD_DATE}/*.rpm ;
do
    echo Building ${SRPM}
    mock -r epel-6-x86_64  rebuild  ${SRPM}
done


