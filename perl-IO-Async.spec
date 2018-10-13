#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-IO-Async
Version  : 0.72
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/IO-Async-0.72.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/IO-Async-0.72.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libi/libio-async-perl/libio-async-perl_0.72-1.debian.tar.xz
Summary  : 'Asynchronous event-driven programming'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-IO-Async-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Future)
BuildRequires : perl(Future::Utils)
BuildRequires : perl(Struct::Dumb)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Identity)
BuildRequires : perl(Test::Refcount)

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

%description dev
dev components for the perl-IO-Async package.


%package license
Summary: license components for the perl-IO-Async package.
Group: Default

%description license
license components for the perl-IO-Async package.


%prep
%setup -q -n IO-Async-0.72
cd ..
%setup -q -T -D -n IO-Async-0.72 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/IO-Async-0.72/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-Async
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-IO-Async/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-IO-Async/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Channel.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Debug.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/File.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/FileStream.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Function.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Future.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Handle.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Internals/ChildManager.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Internals/Connector.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Internals/TimeQueue.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Listener.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Loop.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Loop/Poll.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Loop/Select.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/LoopTests.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Notifier.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/OS.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/OS/MSWin32.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/OS/cygwin.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/OS/linux.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/PID.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Process.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Protocol.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Protocol/LineStream.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Protocol/Stream.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Resolver.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Routine.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Signal.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Socket.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Stream.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Test.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Timer.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Timer/Absolute.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Timer/Countdown.pm
/usr/lib/perl5/vendor_perl/5.26.1/IO/Async/Timer/Periodic.pm

%files dev
%defattr(-,root,root,-)
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
/usr/share/package-licenses/perl-IO-Async/LICENSE
/usr/share/package-licenses/perl-IO-Async/deblicense_copyright
