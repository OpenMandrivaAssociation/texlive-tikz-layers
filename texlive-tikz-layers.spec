Name:		texlive-tikz-layers
Version:	46660
Release:	2
Summary:	TikZ provides graphical layers on TikZ: "behind", "above" and "glass"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikz-layers
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-layers.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-layers.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TikZ-layers is a tiny package that provides, along side
"background", typical graphical layers on TikZ: "behind",
"above" and "glass". The layers may be selected with one of the
styles "on behind layer", "on above layer", "on glass layer" as
an option to a {scope} environment.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-layers
%doc %{_texmfdistdir}/doc/latex/tikz-layers

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
