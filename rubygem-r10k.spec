%{!?ruby_sitelib: %global ruby_sitelib %(ruby -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")}
%{!?ruby_sitearch: %global ruby_sitearch %(ruby -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")}

%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}
%define gemname r10k


Name:           rubygem-%{gemname}
Version:        1.2.0
Release:        1%{?dist}
Summary:        Puppet environment and module deployment

Group:          Development/Languages

License:        ASL 2.0
URL:            https://github.com/adrienthebo/r10k
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  ruby ruby-devel
BuildRequires:  rubygems
Requires:       rubygems
Requires:       ruby(abi) = 1.8
Provides:       rubygem(%{gemname}) = %{version}

%description
r10k provides a general purpose toolset for deploying Puppet 
environments and modules. It implements the Puppetfile format 
and provides a native implementation of Puppet dynamic environments.


%prep

%setup -q -c -T

%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}



%check


%clean
rm -rf  %{buildroot}


%files
%defattr(-,root,root,-)
%doc
# For noarch packages: ruby_sitelib
%{ruby_sitelib}/*
# For arch-specific packages: ruby_sitearch
%{ruby_sitearch}/*


%changelog
