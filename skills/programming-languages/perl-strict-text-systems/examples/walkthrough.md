# Nontrivial Implementation & Multi-File Engineering Walkthrough: `perl-strict-text-systems`

- **Target File**: `examples/strict_log_aggregator.pl`
- **Verification Runner**: `tests/run_verification.py`

## Source Implementation

```
#!/usr/bin/env perl
use v5.36;
use utf8;
use List::Util qw(sum0);

sub parse_kv_line ($line) {
    chomp $line;
    die "Invalid control char in line\n" if $line =~ /[\x00-\x1f]/;
    my %rec;
    for my $pair (split /\s+/, $line) {
        my ($k, $v) = split /=/, $pair, 2;
        die "Malformed token: $pair\n" unless defined $k && defined $v && $k =~ /\A[a-z_]+\z/;
        $rec{$k} = $v;
    }
    return \%rec;
}

my $r1 = parse_kv_line("service=api latency_ms=42 status=200\n");
die "Mismatch" unless $r1->{service} eq 'api' && $r1->{latency_ms} == 42;
my $ok = eval { parse_kv_line("bad;key=1\n"); 1 };
die "Expected rejection of invalid key" if $ok;
say "VERIFIED: Native Perl v5.36 signatures, taint-safe regex & strict parser passed";

```
