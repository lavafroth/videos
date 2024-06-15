#[derive(thiserror::Error)]
pub enum CustomError {
    Io(#[from] std::io::Error),
    Timeout(Duration),
    // ...
}
