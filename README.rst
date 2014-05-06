build_gem_rpm.sh
================

Script that creates spec files and tries to build them from ruby gems with an optional version.

Very non production. It is just something I knocked up so that I could build the rubygem-r10k rpm

Usage::

    bash build_gem_rpm.sh gem_name [version]

Even worse wrapper to build the dependencies of a rubygem rpm:

.. code-block:: bash

	rpm -qi --requires -p /home/tim/public_html/repos/epel-6-x86_64/rubygem-r10k-1.2.1-1.el6.noarch.rpm | \
	grep 'rubygem('|grep '='|sed 's/rubygem(//g;s/) >= / /g' |\
	grep -Ev 'colored|cri |faraday |faraday_middleware |json_pure 1.8.1|r10k|faraday_middleware-multi_json'|\
	while read line ;
	do
		bash build_gem_rpm.sh $line || break ;
	done


