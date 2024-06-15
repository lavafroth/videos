pub trait Error: Debug + Display {
    // Provided methods
    fn source(&self) -> Option<&(dyn Error + 'static)> { /* ... */ }
    fn description(&self) -> &str { /* ... */ }
    fn cause(&self) -> Option<&dyn Error> { /* ... */ }
    fn provide<'a>(&'a self, request: &mut Request<'a>) { /* ... */ }
}
