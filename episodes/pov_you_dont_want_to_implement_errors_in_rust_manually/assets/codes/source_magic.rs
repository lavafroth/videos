use std::error::Error;
use std::{fmt::Display, fs};

#[derive(Debug, thiserror::Error)]
pub enum Ehrah {
    Bruh { source: std::io::Error },
}

impl Display for Ehrah {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "ehrah")
    }
}

fn main() {
    if let Err(e) = fs::read_to_string("nonexistent") {
        let error = Ehrah::Bruh { source: e };
        println!("{:#?}", error.source());
    }
}
