# Generated from r10k-1.1.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name r10k

Name: rubygem-%{gem_name}
Version: 1.1.4
Release: 1%{?dist}
Summary: Puppet environment and module deployment
Group: Development/Languages
License: Apache 2.0
URL: http://github.com/adrienthebo/r10k
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi)
Requires: ruby(rubygems) 
Requires: rubygem(colored) >= 1.2
Requires: rubygem(cri) => 2.4.0
Requires: rubygem(cri) < 2.5
Requires: rubygem(systemu) => 2.5.2
Requires: rubygem(systemu) < 2.6
Requires: rubygem(log4r) >= 1.1.10
Requires: rubygem(json_pure) 
BuildRequires: ruby(abi)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
R10K provides a general purpose toolset for deploying Puppet environments
and modules.
It implements the Puppetfile format and provides a native implementation of
Puppet
dynamic environments.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{gem_instdir}
%{_bindir}/r10k
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%defattr(-,root,root,-)
%doc %{gem_docdir}
%{gem_instdir}/spec
#%{gem_instdir}/doc
%{gem_instdir}/CHANGELOG
%{gem_instdir}/Gemfile
%{gem_instdir}/LICENSE
%{gem_instdir}/README.markdown
#%{gem_instdir}/Rakefile
%{gem_instdir}/r10k.yaml.example
#%{gem_instdir}/r10k.gemspec
%exclude %{gem_instdir}/.gitignore
#%exclude %{gem_instdir}/.nodeset.yml
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/.travis.yml

%{gem_spec}

%changelog
* Mon May 05 2014 Tim Hughes - 1.1.4-1
- Initial package
