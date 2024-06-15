#[cfg(target_os = "windows")]
const HOME_BASE: &str = "C:\\Users\\";

#[cfg(not(target_os = "windows"))]
const HOME_BASE: &str = "/home";

fn main() {
    println!("entering fallback environment at {}", HOME_BASE);
    // ...
}
