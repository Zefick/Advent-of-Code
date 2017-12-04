package adventofcode2015;


public class Day22 {

	static class GameState implements Cloneable {
	    int hp1 = 50;
	    int hp2 = 51;
	    int bossDmg = 9;
	    int shield = 0;
	    int poison = 0;
	    int recharge = 0;
	    int mana = 500;
	    @Override
	    protected GameState clone() {
	    	try {
				return (GameState)super.clone();
			} catch (CloneNotSupportedException e) {
				return null;
			}
	    }
	}

	enum Spell {
		Missile(53) {
            void effect(GameState s) {s.hp2 -= 4;}
		},
		Drain(73) {
            void effect(GameState s) {s.hp1 += 2; s.hp2 -= 2;}
		},
		Shield(113) {
			boolean allowToCast(GameState s) {return s.shield == 0;}
            void effect(GameState s) {s.shield = 6;}
		},
		Poison(173) {
            boolean allowToCast(GameState s) {return s.poison == 0;}
            void effect(GameState s) {s.poison = 6;}
		},
		Recharge(229) {
            boolean allowToCast(GameState s) {return s.recharge == 0;}
            void effect(GameState s) {s.recharge = 5;}
		};
		int cost;
		Spell(int cost) {
			this.cost = cost;
		}
		boolean allowToCast(GameState s) {return true;}
		abstract void effect(GameState s);
	}

	static Integer turn(GameState s, int mana, boolean player) {
		if (player) s.hp1 -= 1;
		if (s.hp1 <= 0) {
			return null;
		}
		if (s.hp2 <= 0) {
			return mana;
		}
		if (s.poison > 0) {
			s.hp2 -= 3;
			if (s.hp2 <= 0) {
				return mana;
			}
			--s.poison;
		}
		if (s.recharge > 0) {
			s.mana += 101;
			--s.recharge;
		}
		s.shield = Math.max(0, s.shield-1);
		if (!player) {
			s.hp1 -= Math.max(1, s.bossDmg - (s.shield > 0 ? 7 : 0));
			if (s.hp1 <= 0) {
				return null;
			}
			return turn(s, mana, true);
		} else {
			Integer min = null;
			for (Spell spell : Spell.values()) {
				if (spell.allowToCast(s) && s.mana >= spell.cost) {
					GameState s2 = s.clone();
					s2.mana -= spell.cost;
					spell.effect(s2);
					Integer n = turn(s2, mana+spell.cost, false);
					if (n != null) {
						min = min == null ? n : Math.min(min, n);
					}
				}
			}
			return min;
		}
	}

	public static void main(String[] args) throws Exception {
	    GameState state = new GameState();
	    Integer best = turn(state, 0, true);
	    System.out.println(best);
	}

}
