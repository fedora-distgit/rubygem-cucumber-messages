# Generated from cucumber-messages-14.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name cucumber-messages

Name: rubygem-%{gem_name}
Version: 14.0.1
Release: 1.4%{?dist}
Summary: cucumber-messages-14.0.1
License: MIT
URL: https://github.com/cucumber/messages-ruby#readme
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.3
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(protobuf)
BuildArch: noarch

%description
Protocol Buffer messages for Cucumber's inter-process communication.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/VERSION
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec

%changelog
* Wed Oct 28 2020 Pavel Valena <pvalena@redhat.com> - 14.0.1-1
- Initial package
