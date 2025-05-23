#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v25
# autospec commit: 9594167
#
Name     : perl-IO-Async
Version  : 0.804
Release  : 47
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/IO-Async-0.804.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/IO-Async-0.804.tar.gz
Summary  : 'Asynchronous event-driven programming'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-IO-Async-license = %{version}-%{release}
Requires: perl-IO-Async-perl = %{version}-%{release}
Requires: perl(Future)
Requires: perl(Future::IO::ImplBase)
Requires: perl(Future::Utils)
Requires: perl(Struct::Dumb)
Requires: perl(Test::Fatal)
Requires: perl(Test::Metrics::Any)
Requires: perl(Test::Refcount)
BuildRequires : buildreq-cpan
BuildRequires : perl(Future)
BuildRequires : perl(Future::Utils)
BuildRequires : perl(Struct::Dumb)
BuildRequires : perl(Test::Future::IO::Impl)
BuildRequires : perl(Test::Metrics::Any)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
IO::Async - Asynchronous event-driven programming
SYNOPSIS
use IO::Async::Stream;
use IO::Async::Loop;

my $loop = IO::Async::Loop->new;

$loop->connect(
host     => "some.other.host",
service  => 12345,
socktype => 'stream',

on_stream => sub {
my ( $stream ) = @_;

$stream->configure(
on_read => sub {
my ( $self, $buffref, $eof ) = @_;

while( $$buffref =~ s/^(.*\n)// ) {
print "Received a line $1";
}

return 0;
}
);

$stream->write( "An initial line here\n" );

$loop->add( $stream );
},

on_resolve_error => sub { die "Cannot resolve - $_[-1]\n"; },
on_connect_error => sub { die "Cannot connect - $_[0] failed $_[-1]\n"; },
);

$loop->run;

%package dev
Summary: dev components for the perl-IO-Async package.
Group: Development
Provides: perl-IO-Async-devel = %{version}-%{release}
Requires: perl-IO-Async = %{version}-%{release}

%description dev
dev components for the perl-IO-Async package.


%package license
Summary: license components for the perl-IO-Async package.
Group: Default

%description license
license components for the perl-IO-Async package.


%package perl
Summary: perl components for the perl-IO-Async package.
Group: Default
Requires: perl-IO-Async = %{version}-%{release}

%description perl
perl components for the perl-IO-Async package.


%prep
%setup -q -n IO-Async-0.804
cd %{_builddir}/IO-Async-0.804
pushd ..
cp -a IO-Async-0.804 buildavx2
popd
pushd ..
cp -a IO-Async-0.804 buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-Async
cp %{_builddir}/IO-Async-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-IO-Async/c1cfcc0e8c1fbc9bc21bceecbf46050249ed3ebf || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Future::IO::Impl::IOAsync.3
/usr/share/man/man3/IO::Async.3
/usr/share/man/man3/IO::Async::Channel.3
/usr/share/man/man3/IO::Async::Debug.3
/usr/share/man/man3/IO::Async::File.3
/usr/share/man/man3/IO::Async::FileStream.3
/usr/share/man/man3/IO::Async::Function.3
/usr/share/man/man3/IO::Async::Future.3
/usr/share/man/man3/IO::Async::Handle.3
/usr/share/man/man3/IO::Async::Listener.3
/usr/share/man/man3/IO::Async::Loop.3
/usr/share/man/man3/IO::Async::Loop::Poll.3
/usr/share/man/man3/IO::Async::Loop::Select.3
/usr/share/man/man3/IO::Async::LoopTests.3
/usr/share/man/man3/IO::Async::Metrics.3
/usr/share/man/man3/IO::Async::Notifier.3
/usr/share/man/man3/IO::Async::OS.3
/usr/share/man/man3/IO::Async::OS::MSWin32.3
/usr/share/man/man3/IO::Async::OS::cygwin.3
/usr/share/man/man3/IO::Async::OS::linux.3
/usr/share/man/man3/IO::Async::PID.3
/usr/share/man/man3/IO::Async::Process.3
/usr/share/man/man3/IO::Async::Protocol.3
/usr/share/man/man3/IO::Async::Protocol::LineStream.3
/usr/share/man/man3/IO::Async::Protocol::Stream.3
/usr/share/man/man3/IO::Async::Resolver.3
/usr/share/man/man3/IO::Async::Routine.3
/usr/share/man/man3/IO::Async::Signal.3
/usr/share/man/man3/IO::Async::Socket.3
/usr/share/man/man3/IO::Async::Stream.3
/usr/share/man/man3/IO::Async::Test.3
/usr/share/man/man3/IO::Async::Timer.3
/usr/share/man/man3/IO::Async::Timer::Absolute.3
/usr/share/man/man3/IO::Async::Timer::Countdown.3
/usr/share/man/man3/IO::Async::Timer::Periodic.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-Async/c1cfcc0e8c1fbc9bc21bceecbf46050249ed3ebf

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
