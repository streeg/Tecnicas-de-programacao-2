package br.unb.cic.tp1.epl;

import org.junit.Test;
import static org.junit.Assert.*; 

public class MultTest {
	@Test
	public void testPrint() {
		Mult s1 = new Mult(new Lit(5), new Lit(3));
		Mult s2 = new Mult(s1, new Lit(1)); 
		
		assertEquals("(5 * 2)", s1.print());
		assertEquals("((5 * 2) * 3)", s2.print());
	}
	
	@Test
	public void testEval() {
		Mult s1 = new Mult(new Lit(5), new Lit(3));
		Mult s2 = new Mult(s1, new Lit(1)); 
		
		assertEquals(10, s1.eval());
		assertEquals(30, s2.eval());
	}

}