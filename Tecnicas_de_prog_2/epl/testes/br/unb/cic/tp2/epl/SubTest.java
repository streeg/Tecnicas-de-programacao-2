package br.unb.cic.tp1.epl;

import org.junit.Test;
import static org.junit.Assert.*; 

public class SubTest {
	@Test
	public void testPrint() {
		Sub s1 = new Sub(new Lit(5), new Lit(2));
		Sub s2 = new Sub(s1, new Lit(1)); 
		
		assertEquals("(5 - 2)", s1.print());
		assertEquals("((5 - 2) - 1)", s2.print());
	}
	
	@Test
	public void testEval() {
		Sub s1 = new Sub(new Lit(5), new Lit(2));
		Sub s2 = new Sub(s1, new Lit(1)); 
		
		assertEquals(3, s1.eval());
		assertEquals(2, s2.eval());
	}

}