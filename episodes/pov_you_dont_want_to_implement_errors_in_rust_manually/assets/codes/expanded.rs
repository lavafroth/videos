pub enum ParseError {
    #[error("unable to parse grammar from invalid contents")]
    Grammar(#[from] Box<pest::error::Error<Rule>>),
    #[error("hotkey config must contain one and only one main section")]
    MainSection,
}
#[automatically_derived]
impl ::core::fmt::Debug for ParseError {
    #[inline]
    fn fmt(&self, f: &mut ::core::fmt::Formatter) -> ::core::fmt::Result {
        match self {
            ParseError::Grammar(__self_0) => {
                ::core::fmt::Formatter::debug_tuple_field1_finish(f, "Grammar", &__self_0)
            }
            ParseError::MainSection => ::core::fmt::Formatter::write_str(f, "MainSection"),
        }
    }
}
