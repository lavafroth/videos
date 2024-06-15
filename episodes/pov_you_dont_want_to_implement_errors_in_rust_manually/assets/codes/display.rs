pub trait Display {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result;
}
