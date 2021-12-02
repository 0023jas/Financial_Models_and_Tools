/*
This module file is used to separate the API keys from main.rs
by doing this, the main file is looking less like unorganised code,
*/

/* Example code of what a buy and sell market order would consist of in code. */
//client.buy_market_funds("ETH-GBP", 10.0).expect("Could not buy market funds");
//client.sell_market_funds("ETH-GBP", 10.11).expect("Could not sell market");

/*
loop {
    client
        .buy_market_funds("ETH-GBP", 10.0)
        .expect("could not buy market funds");
    client
        .sell_market_funds("ETH-GBP", 10.11)
        .expect("Could not sell market funds");
    thread::sleep(Duration::from_millis(200))
}
*/

/*
    println!("Great British Pound: ");
    let gbp = accounts.iter().find(|x| x.currency == "GBP").unwrap();
    println!("{}.  balance: {:?}", gbp.currency, gbp.balance);
    println!("{}.available: {:?}", gbp.currency, gbp.available);
    println!("{}.     hold: {:?}", gbp.currency, gbp.hold);
    thread::sleep(Duration::from_millis(200));
    */

pub fn key() -> &'static str {
    static KEY: &str = "";
    KEY
}

pub fn secret() -> &'static str {
    static SECRET: &str =
        "";
    SECRET
}

pub fn passphrase() -> &'static str {
    static PASSPHRASE: &str = "";
    PASSPHRASE
}
