function names(a,b,c) {
	var d = Number(c.value);
	if (d == 1) {
		alert(Number(a.value) + Number(b.value))
	} else {
		if (d == 2) {
			alert(Number(a.value) - Number(b.value))
		} else {
			if (d == 3) {
				alert(Number(a.value) * Number(b.value))
			} else {
				if (d == 4) {
					alert(Number(a.value) / Number(b.value))
				}
			}
		}
	}
}
