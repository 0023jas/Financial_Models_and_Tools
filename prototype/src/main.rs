/*
This is the prototype of the Rust bot project
*/

use coinbase_pro_rs::{Private, Sync, SANDBOX_URL};
use std::thread;
use std::time::Duration;

//I have created this module to remove the unnecessary keys from the main
//code.
mod keys;
use keys::{key, passphrase, secret};
fn main() {
    let client: Private<Sync> = Private::new(SANDBOX_URL, key(), secret(), passphrase());
    //Rust variable of the account from the client.
    let accounts = client.get_accounts().unwrap();

    //Displays balance before the algorithm starts
    println!("United States Dollar:");
    let usd = accounts.iter().find(|x| x.currency == "USD").unwrap();
    println!("{}.  balance: {:?}", usd.currency, usd.balance);
    println!("{}.available: {:?}", usd.currency, usd.available);
    println!("{}.     hold: {:?}", usd.currency, usd.hold);

    let mut number_of_trades: i32 = 1;
    loop {
        //Selection statement for if the number of trades finish,
        //Then the program finishes.
        if number_of_trades == 3600 {
            println!("[Finishing]");
            break;
        } else {
            //Buying $10 worth of bitcoin.
            client
                .buy_market_funds("BTC-USD", 10.00)
                .expect("Could not buy_market_funds");
            //Selling $10.11 worth of bitcoin.
            client
                .sell_market_funds("BTC-USD", 10.11)
                .expect("Could not sell_market_funds");

            number_of_trades += 1;

            //Stop Loss function.
            if usd.balance <= 5.00 {
                println!("[Breaking loop]");
                break;
            }
        }
        //Using thread::sleep to keep clear of the rate limits
        thread::sleep(Duration::from_millis(200));
    }

    //Displays balance once the algorithm finishes
    println!("United States Dollar:");
    let usd = accounts.iter().find(|x| x.currency == "USD").unwrap();
    println!("{}.  balance: {:?}", usd.currency, usd.balance);
    println!("{}.available: {:?}", usd.currency, usd.available);
    println!("{}.     hold: {:?}", usd.currency, usd.hold);
}
