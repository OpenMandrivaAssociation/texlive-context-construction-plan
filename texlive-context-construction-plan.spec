Name:		texlive-context-construction-plan
Version:	47085
Release:	2
Summary:	Construction plans in ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-construction-plan
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-construction-plan.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-construction-plan.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
Generate a page with a figure at a well-defined scale.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/construction-plan
%doc %{_texmfdistdir}/doc/context/third/construction-plan

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
