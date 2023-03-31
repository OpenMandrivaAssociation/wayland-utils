Summary:        Wayland utilities
Name:           wayland-utils
Version:        1.1.0
Release:        2
Group:        	System/Libraries
License:        MIT
URL:            https://wayland.freedesktop.org/
Source0:        https://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(wayland-scanner)

%description
wayland-utils contains wayland-info, a standalone version of weston-info,
a utility for displaying information about the Wayland protocols supported
by the Wayland compositor.
wayland-info also provides additional information for a subset of Wayland
protocols it knows about, namely Linux DMABUF, presentation time, tablet and
XDG output protocols.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_bindir}/wayland-info
%doc %{_mandir}/man1/wayland-info.1*
