Summary:	Qt GUI for dvda-author
Name:		dvda-author-gui
Version:	09.02
Release:	%mkrel 2
Source0:	%{name}-%{version}-13.tar.gz
License:	GPLv3
Group: 		Archiving/Cd burning
BuildRoot:	%{_builddir}/%{name}-%{version}-%{release}-buildroot
Requires:	dvda-author
BuildRequires:	qt4-devel

%description
dvda-author-gui is a Qt4 GUI for dvda-author.

%prep
%setup -q

%build
%qmake_qt4
%make
mv gui dvda-author-gui
sed -e 's#/usr/local/share#%{_datadir}#g' -i %{name}.desktop

%install
rm -rf %{buildroot}

install -m644 images/dvda-author.png -D %{buildroot}%{_datadir}/pixmaps/dvda-author.png
install -m644 %{name}.desktop -D %{buildroot}%{_datadir}/applications/%{name}.desktop
install -m755 %{name} -D %{buildroot}%{_bindir}/%{name}
cp -rf images/ %{buildroot}%{_datadir}/%{name}
cp -f GUI.shtml %{buildroot}%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/dvda-author.png

