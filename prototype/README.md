## Prototype

This is the prototype for the trading bot built in Rust.

## Description

Rust offers vaulable advantages due to concurrency and
operating without a garbage collector and making
use of the package manager Cargo.

The aim is to build a trading bot from Rust that holds
a advantage in terms of speed when trading.

## Why not other languages?

Languages such as Go is a garbage collected program and can
suffer from latency spikes. The company Discord has an article
on explaining this problem and why Rust solved it.

The Python programming language is a very good language for
quickly creating a bot however performance wise, due to the language.
being interpreted, this can slow the trading bot down.

Java is also a good language but Java's memory management is
garbage collected.

C++ would be the only good option however, since the benchmark games test 
on Rust vs C++. Rust has proved to be outperform C++ in various aspects.

The only reason why quantitative firms choose C++ is because they are
familar with C++ and do not want to waste time re-writing the code in Rust.

## How will this bot be hosted?

Coinbase Pro data centers are in the Amazon US East N. Virginia (us-east-1) region.
Using a Virtual Private server in AWS, I can locate the server in the us-east-1
region. 

As a result of the server location, this reduces latency to and from the exchange and
the server.

Coinbase Pro operates a continuous first-come, first-serve order book.
Orders are executed in price-time priority as received by the matching engine.

Therefore by hosting the bot closest to the exchange as well as using a language that
is memory-safe and concurrent. The bot can trade without any fuss and latency.

## References

Benchmark games:
Rust vs C++:
https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/rust-gpp.html
Rust vs Go:
https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/rust-go.html

Why Discord is switching from Go to Rust:
https://blog.discord.com/why-discord-is-switching-from-go-to-rust-a190bbca2b1f