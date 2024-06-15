impl std::error::Error for CustomError {};
impl std::fmt::Display for CustomError {
    fn fmt(&self,
    f: &mut std::fmt::Formatter) -> std::fmt::Result {
        // ...
    }
}
