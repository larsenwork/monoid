perl -i -nle 'print if !/^Substitution2\b/' ~/git/Monoid-Master/Source/*/*.glyph
perl -i -nle 'print if !/^Ligature2\b/' ~/git/Monoid-Master/Source/*/*.glyph
perl -i -nle 'print if !/^Lookup\b/' ~/git/Monoid-Master/Source/*/font.props
sed -i '' '/ChainSub2/,/EndFPST/d' ~/git/Monoid-Master/Source/*/font.props