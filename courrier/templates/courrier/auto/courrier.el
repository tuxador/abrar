(TeX-add-style-hook
 "courrier"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("letter" "11pt" "a4paper")))
   (TeX-run-style-hooks
    "latex2e"
    "letter"
    "letter11"
    "graphicx"
    "microtype"
    "fontspec"
    "polyglossia"
    "xltxtra")
   (TeX-add-symbols
    "vhrulefill"
    "Who"
    "What"
    "Where"
    "Address"
    "CityZip"
    "Email"
    "TEL"
    "URL"
    "opening"
    "closing")
   (LaTeX-add-polyglossia-langs
    '("french" "mainlanguage" "")))
 :latex)

