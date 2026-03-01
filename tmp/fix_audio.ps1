$files = @(
    "vocab_sets/4b/index.html",
    "vocab_sets/kitchen_kids/index.html"
)

foreach ($file in $files) {
    if (Test-Path $file) {
        $content = Get-Content $file -Raw -Encoding UTF8
        # Add the helper function if not exists
        if ($content -notmatch "function playEncodedAudio") {
            $helper = "
        function playEncodedAudio(encoded) {
            speak(decodeURIComponent(encoded));
        }
        function speak(text) {"
            $content = $content -replace "function speak\(text\) \{", $helper
        }
        
        # Replace speak(xxx) with playEncodedAudio(encodeURIComponent(xxx))
        # Front card
        $content = $content -replace "speak\('`\$\{vocab.word.replace\(/'/g, ""\\\'""\)\}'\)", "playEncodedAudio('`${encodeURIComponent(vocab.word)}')`""

        # Back card (Word)
        # We need to aggressively replace any speak(xxx) to be safe because of single quotes.
        # Actually, let's just do regex for the specific lines.
        $content = $content -replace "speak\('`\$\{vocab\.word[^}]*\}'\)", "playEncodedAudio('`${encodeURIComponent(vocab.word)}')`""
        $content = $content -replace "speak\('`\$\{vocab\.ex_en[^}]*\}'\)", "playEncodedAudio('`${encodeURIComponent(vocab.ex_en)}')`""
        
        Set-Content -Path $file -Value $content -Encoding UTF8
    }
}

# Convert 4A page
$legacyFile = "index-legacy-before-expression.html"
$new4aDir = "vocab_sets/4a"
if (Test-Path $legacyFile) {
    New-Item -ItemType Directory -Force -Path $new4aDir | Out-Null
    $content16 = Get-Content $legacyFile -Raw -Encoding Unicode
    
    # Fix audio buttons in 4A page as well
    if ($content16 -notmatch "function playEncodedAudio") {
        $helper4a = "
        function playEncodedAudio(encoded) {
            speak(decodeURIComponent(encoded));
        }
        function speak(text) {"
        $content16 = $content16 -replace "function speak\(text\) \{", $helper4a
    }
    
    $content16 = $content16 -replace "speak\('`\$\{vocab\.word[^}]*\}'\)", "playEncodedAudio('`${encodeURIComponent(vocab.word)}')`""
    $content16 = $content16 -replace "speak\('`\$\{vocab\.ex_en[^}]*\}'\)", "playEncodedAudio('`${encodeURIComponent(vocab.ex_en)}')`""

    Set-Content -Path "$new4aDir/index.html" -Value $content16 -Encoding UTF8
}
