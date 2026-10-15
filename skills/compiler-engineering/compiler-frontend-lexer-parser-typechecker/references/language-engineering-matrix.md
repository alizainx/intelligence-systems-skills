# Pratt Parsing & Hindley-Milner Type Inference Reference

Omitting the occurs check allows self-application `fn x => x(x)` to loop forever during type substitution.
