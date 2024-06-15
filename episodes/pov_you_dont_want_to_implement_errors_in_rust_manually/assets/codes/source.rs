use thiserror::Error;

#[derive(Debug, Error)]
pub enum Ehrah {
    Bruh {
        #[from]
        bruh: std::io::Error,
        #[source]
        sike: String,
    },
}

fn main() {
    println!("Hello, world!");
}
