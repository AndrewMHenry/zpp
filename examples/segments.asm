.namespace app

.segment safeRam
.property type "variable"
.property start 0x86EC
.property size 768
.end safeRam

.segment appSegment
.property type "code"
.property start 0x4000
.property size 0x4000
.end appSegment

.variable-segment safeRam
.base 0x86EC
.size 768
.end safeRam

.code-segment appSegment
.base 0x4000
.size 0x4000
.end appSegment

.variable-segment mytable
.align 256
.size 256
.end mytable

.end app
