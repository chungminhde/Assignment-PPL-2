import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_AST_0(self):
        input = """int a;
        int foo(int a)
        {
            int b;
            a;
            c;
        }
                    """
        expect= str()
        self.assertTrue(TestAST.checkASTGen(input,expect,300))
    # def test_AST_1(self):
    #     input = """int a;
    #                 """
    #     expect = str(Program([VarDecl('a',IntType())]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,301))
    # def test_AST_2(self):
    #     input = """int a[10];
    #                 """
    #     expect = str(Program([VarDecl('a',ArrayType(10,IntType()))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,302))
    # def test_AST_3(self):
    #     input = """boolean a[10];
    #                 """
    #     expect = str(Program([VarDecl('a',ArrayType(10,BoolType()))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,303))
    # def test_AST_4(self):
    #     input = """float a,b,c;
    #     """
    #     expect = str(Program([VarDecl("a",FloatType()),VarDecl("b",FloatType()),VarDecl("c",FloatType())]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,304))
    # def test_AST_5(self):
    #     input = """boolean a[5];
    #     """
    #     expect = str(Program([VarDecl("a",ArrayType(5,BoolType()))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,305))
    # def test_AST_6(self):
    #     input = """int a,b[5],c;
    #     """
    #     expect = str(Program([VarDecl("a",IntType()),VarDecl("b",ArrayType(5,IntType())),VarDecl("c",IntType())]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,306))
    # def test_AST_7(self):
    #     input = """int a; int b;
    #     """
    #     expect = str(Program([VarDecl('a',IntType()),VarDecl('b',IntType())]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,307))
    # def test_AST_8(self):
    #     input = """int main(){}
    #     """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,308))
    # def test_AST_9(self):
    #     input = """int main () {
    #         int a;
    #     }"""
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType())]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,309))
    # def test_AST_10(self):
    #     input = """int main () {
    #         getIntLn();
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,310))
    # def test_AST_11(self):
    #     input = """int main () {
    #         int a,b,c;
    #     }"""
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',IntType())]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,311))
    # def test_AST_12(self):
    #     input = """int main(){
    #         foo();
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('foo'),[])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,312))
    # def test_AST_13(self):
    #     input = """ int a,b,c[2];
    #     float f[10];
    #     boolean bool;
    #     string main(){}
    #                 """
    #     expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",ArrayType(2,IntType())),VarDecl("f",ArrayType(10,FloatType())),VarDecl("bool",BoolType()),FuncDecl(Id("main"),[],StringType(),Block([]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,313))
    # def test_AST_14(self):
    #     input = """float exception(boolean a){
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id("exception"),[VarDecl("a",BoolType())],FloatType(),Block([]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,314))
    # def test_AST_15(self):
    #     input = """float exception(boolean a,int b){
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('exception'),[VarDecl('a',BoolType()),VarDecl('b',IntType())],FloatType(),Block([]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,315))
    
    # def test_AST_16(self):
    #     input = """ int main() {
    #         boolean test;
    #         test = true;
    #     }"""
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('test',BoolType()),BinaryOp('=',Id('test'),BooleanLiteral(True))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,316))
    # def test_AST_17(self):
    #     input = """ 
    #         int a;
    #         int prime(int n){}
    #     """
    #     expect = str(Program([VarDecl('a',IntType()),FuncDecl(Id('prime'),[VarDecl('n',IntType())],IntType(),Block([]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,317))
    # def test_AST_18(self):
    #     input = """ 
    #         int a;
    #         int prime(int n){
    #             int b;
    #         }
    #     """
    #     expect = str(Program([VarDecl('a',IntType()),FuncDecl(Id('prime'),[VarDecl('n',IntType())],IntType(),Block([VarDecl('b',IntType())]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,318))
    # def test_AST_19(self):
    #     input = """ 
    #         int a;
    #         int prime(int n){
    #             int b;
    #         }
    #         int main(){
    #             prime(5);
    #         }
    #     """
    #     expect = str(Program([VarDecl('a',IntType()),FuncDecl(Id('prime'),[VarDecl('n',IntType())],IntType(),Block([VarDecl('b',IntType())])),FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('prime'),[IntLiteral(5)])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,319))
    # def test_AST_20(self):
    #     input = """int a,b,c,d,e;
    #                 float x,y,z;
    #                 int main()
    #                 {

    #                 }
    #                 """
    #     expect = str(Program([VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',IntType()),VarDecl('d',IntType()),VarDecl('e',IntType()),VarDecl('x',FloatType()),VarDecl('y',FloatType()),VarDecl('z',FloatType()),FuncDecl(Id('main'),[],IntType(),Block([]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,320))
    # def test_AST_21(self):
    #     input = """int main() {
    #         int a;
    #         a=10000;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),BinaryOp('=',Id('a'),IntLiteral(10000))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,321))
    # def test_AST_22(self):
    #     input = """boolean test;
    #         void main()
    #         {
    #             if(test)
    #                 a=b+c;
    #         }
    #                 """
    #     expect = str(Program([VarDecl('test',BoolType()),FuncDecl(Id('main'),[],VoidType(),Block([If(Id('test'),BinaryOp('=',Id('a'),BinaryOp('+',Id('b'),Id('c'))))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,322))
    # def test_AST_23(self):
    #     input = """int main() {
    #         printf("Nightmare");
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('printf'),[StringLiteral('Nightmare')])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,323))
    # def test_AST_24(self):
    #     input = """int main() {
    #         do
    #         {
                
    #         }
    #         while(a);
        
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([Block([])],Id('a'))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,324))
    # def test_AST_25(self):
    #     input = """int main() {
    #         if(a>b) 
    #             printf(a>b);
    #         else
    #             a=b;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('>',Id('a'),Id('b')),CallExpr(Id('printf'),[BinaryOp('>',Id('a'),Id('b'))]),BinaryOp('=',Id('a'),Id('b')))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,325))
    # def test_AST_26(self):
    #     input = """int main() {
    #         int i;
    #         for(i;i<n;i+1)
    #             printf("%d",i);
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('i',IntType()),For(Id('i'),BinaryOp('<',Id('i'),Id('n')),BinaryOp('+',Id('i'),IntLiteral(1)),CallExpr(Id('printf'),[StringLiteral('%d'),Id('i')]))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,326))
    # def test_AST_27(self):
    #     input = """int main() {
    #         do 
    #         {
    #             return; 
    #         }
    #         while(a!=0);
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([Block([Return()])],BinaryOp('!=',Id('a'),IntLiteral(0)))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,327))
    # def test_AST_28(self):
    #     input = """int x,y;
    #     int main() {
    #         x=y;
    #     }
    #                 """
    #     expect = str(Program([VarDecl('x',IntType()),VarDecl('y',IntType()),FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('x'),Id('y'))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,328))
    # def test_AST_29(self):
    #     input = """int main(){
    #     }
    #     void putInt(int f)
    #     {
    #         return 5;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([])),FuncDecl(Id("putInt"),[VarDecl("f",IntType())],VoidType(),Block([Return(IntLiteral(5))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,329))
    # def test_AST_30(self):
    #     input = """int foo(int k) {k=k+1;}
    #     int main() {
    #         foo(5);
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('foo'),[VarDecl('k',IntType())],IntType(),Block([BinaryOp('=',Id('k'),BinaryOp('+',Id('k'),IntLiteral(1)))])),FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('foo'),[IntLiteral(5)])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,330))
    # def test_AST_31(self):
    #     input = """int main() {
    #         int x,arr[100];
    #         arr[x+3]=5;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('x',IntType()),VarDecl('arr',ArrayType(100,IntType())),BinaryOp('=',ArrayCell(Id('arr'),BinaryOp('+',Id('x'),IntLiteral(3))),IntLiteral(5))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,331))
    # def test_AST_32(self):
    #     input = """int main() {
    #         boolean c;
    #         int i;
    #         if(c)
    #             return;
    #         else 
    #             i=i+100;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('c',BoolType()),VarDecl('i',IntType()),If(Id('c'),Return(),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(100))))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,332))
    # def test_AST_33(self):
    #     input = """int prime(int n)
    #     {
    #         if(n<2)
    #         return 1;
    #     }
    #     int main() {}
    #                 """
    #     expect = str(Program([FuncDecl(Id('prime'),[VarDecl('n',IntType())],IntType(),Block([If(BinaryOp('<',Id('n'),IntLiteral(2)),Return(IntLiteral(1)))])),FuncDecl(Id('main'),[],IntType(),Block([]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,333))
    # def test_AST_34(self):
    #     input = """
    #                 void test(int k)
    #     {
    #         return;
    #     }
    #     int main() {
    #         test(1000);
    #     }"""
    #     expect = str(Program([FuncDecl(Id('test'),[VarDecl('k',IntType())],VoidType(),Block([Return()])),FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('test'),[IntLiteral(1000)])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,334))
    # def test_AST_35(self):
    #     input = """int main()
    #     {
    #         int i;
    #         for(i;i<n;i+1)
    #             {

    #             }
    #             {

    #             }
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('i',IntType()),For(Id('i'),BinaryOp('<',Id('i'),Id('n')),BinaryOp('+',Id('i'),IntLiteral(1)),Block([])),Block([])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,335))
    # def test_AST_36(self):
    #     input = """int main()
    #     {
    #         int i;
    #         for(i;i<n;i+1)
    #             {
    #                 printf("ABCD");
    #                 foo(5);
    #             }
    #             {
    #                 break;
    #             }
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('i',IntType()),For(Id('i'),BinaryOp('<',Id('i'),Id('n')),BinaryOp('+',Id('i'),IntLiteral(1)),Block([CallExpr(Id('printf'),[StringLiteral('ABCD')]),CallExpr(Id('foo'),[IntLiteral(5)])])),Block([Break()])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,336))
    # def test_AST_37(self):
    #     input = """int main()
    #     {
    #         int i;
    #         for(i;i<n;i+1)
    #             {
    #                 test(1.2,5);
    #             }
    #             {
    #                 prime(1,2,3,4,5);
                
    #             }
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('i',IntType()),For(Id('i'),BinaryOp('<',Id('i'),Id('n')),BinaryOp('+',Id('i'),IntLiteral(1)),Block([CallExpr(Id('test'),[FloatLiteral(1.2),IntLiteral(5)])])),Block([CallExpr(Id('prime'),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)])])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,337))
    # def test_AST_38(self):
    #     input = """int main()
    #     {
    #         string f;
    #         f="abcd";
    #         if(f=="abcd")
    #             printf("True");
    #         else
    #             printf("Flase");
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('f',StringType()),BinaryOp('=',Id('f'),StringLiteral('abcd')),If(BinaryOp('==',Id('f'),StringLiteral('abcd')),CallExpr(Id('printf'),[StringLiteral('True')]),CallExpr(Id('printf'),[StringLiteral('Flase')]))]))])   )
    #     self.assertTrue(TestAST.checkASTGen(input,expect,338))
    # def test_AST_39(self):
    #     input = """void abc(int k)
    #     {

    #     }
    #     int main()
    #     {
    #         if(a<b)
    #             abc(a);
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('abc'),[VarDecl('k',IntType())],VoidType(),Block([])),FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('<',Id('a'),Id('b')),CallExpr(Id('abc'),[Id('a')]))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,339))
    # def test_AST_40(self):
    #     input = """int main()
    #     {
    #         //print Hello !!!
    #         printf("Hello !!!");
    #         return;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('printf'),[StringLiteral('Hello !!!')]),Return()]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,340))
    # def test_AST_41(self):
    #     input = """void max(int a, int b)
    #     {
    #         if(a>b)
    #             return a;
    #         else 
    #             return b;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('max'),[VarDecl('a',IntType()),VarDecl('b',IntType())],VoidType(),Block([If(BinaryOp('>',Id('a'),Id('b')),Return(Id('a')),Return(Id('b')))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,341))
    # def test_AST_42(self):
    #     input = """int main()
    #     {
    #         a=(b+c -d[e] ) % f + 1000;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('+',BinaryOp('%',BinaryOp('-',BinaryOp('+',Id('b'),Id('c')),ArrayCell(Id('d'),Id('e'))),Id('f')),IntLiteral(1000)))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,342))
    # def test_AST_43(self):
    #     input = """int main()
    #     {
    #         if(a<b||a<c||c<d)
    #         a = a + d;
    #         else 
    #         {
    #             printf("K");
    #         }
           
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('||',BinaryOp('||',BinaryOp('<',Id('a'),Id('b')),BinaryOp('<',Id('a'),Id('c'))),BinaryOp('<',Id('c'),Id('d'))),BinaryOp('=',Id('a'),BinaryOp('+',Id('a'),Id('d'))),Block([CallExpr(Id('printf'),[StringLiteral('K')])]))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,343))
    # def test_AST_44(self):
    #     input = """int main()
    #     {
    #         a = b || c && d;
    #         int k;
    #         k= a + max(a,b) - min(e,f)/100;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('a'),BinaryOp('||',Id('b'),BinaryOp('&&',Id('c'),Id('d')))),VarDecl('k',IntType()),BinaryOp('=',Id('k'),BinaryOp('-',BinaryOp('+',Id('a'),CallExpr(Id('max'),[Id('a'),Id('b')])),BinaryOp('/',CallExpr(Id('min'),[Id('e'),Id('f')]),IntLiteral(100))))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,344))
    # def test_AST_45(self):
    #     input = """float a,b;
    #     int x,y;
    #     int main()
    #     {
    #         x=x+1;
    #         y=x*y;
    #         if(x<y)
    #             x=true;
    #         else 
    #             y=true;
    #     }
    #                 """
    #     expect = str(Program([VarDecl('a',FloatType()),VarDecl('b',FloatType()),VarDecl('x',IntType()),VarDecl('y',IntType()),FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',Id('x'),BinaryOp('+',Id('x'),IntLiteral(1))),BinaryOp('=',Id('y'),BinaryOp('*',Id('x'),Id('y'))),If(BinaryOp('<',Id('x'),Id('y')),BinaryOp('=',Id('x'),BooleanLiteral(True)),BinaryOp('=',Id('y'),BooleanLiteral(True)))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,345))
    # def test_AST_46(self):
    #     input = """int main()
    #     {
    #         do{
    #         int i;
    #         for(i;i<n;i+1)
    #         printf("Hello");
    #         if(k!=0)
    #         k=k*k;

    #         }
    #         while  a<(b*9/7)  ;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([Dowhile([Block([VarDecl('i',IntType()),For(Id('i'),BinaryOp('<',Id('i'),Id('n')),BinaryOp('+',Id('i'),IntLiteral(1)),CallExpr(Id('printf'),[StringLiteral('Hello')])),If(BinaryOp('!=',Id('k'),IntLiteral(0)),BinaryOp('=',Id('k'),BinaryOp('*',Id('k'),Id('k'))))])],BinaryOp('<',Id('a'),BinaryOp('/',BinaryOp('*',Id('b'),IntLiteral(9)),IntLiteral(7))))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,346))
    # def test_AST_47(self):
    #     input = """boolean test;
    #     int main()
    #     {
    #         int x;
    #         if(test)
    #             x=x+1;
    #         float y;
    #         y=y*15/20 + 1000;
    #     }
    #                 """
    #     expect = str(Program([VarDecl('test',BoolType()),FuncDecl(Id('main'),[],IntType(),Block([VarDecl('x',IntType()),If(Id('test'),BinaryOp('=',Id('x'),BinaryOp('+',Id('x'),IntLiteral(1)))),VarDecl('y',FloatType()),BinaryOp('=',Id('y'),BinaryOp('+',BinaryOp('/',BinaryOp('*',Id('y'),IntLiteral(15)),IntLiteral(20)),IntLiteral(1000)))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,347))
    # def test_AST_48(self):
    #     input = """int[] foo(int a, float b[]) {
    #         int c[3];
    #      if (a>0) 
    #      foo(a-1,b);
    #       return c; }
    #     int main()
    #     {
    #         int c[3];
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',IntType()),VarDecl('b',ArrayPointerType(FloatType()))],ArrayPointerType(IntType()),Block([VarDecl('c',ArrayType(3,IntType())),If(BinaryOp('>',Id('a'),IntLiteral(0)),CallExpr(Id('foo'),[BinaryOp('-',Id('a'),IntLiteral(1)),Id('b')])),Return(Id('c'))])),FuncDecl(Id('main'),[],IntType(),Block([VarDecl('c',ArrayType(3,IntType()))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,348))
    # def test_AST_49(self):
    #     input = """ int main()
    #     {
    #         int x[100];
    #         x[a[b[c]]]= 10;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('x',ArrayType(100,IntType())),BinaryOp('=',ArrayCell(Id('x'),ArrayCell(Id('a'),ArrayCell(Id('b'),Id('c')))),IntLiteral(10))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,349))
    # def test_AST_50(self):
    #     input = """void a(float x)
    #     {
    #         if(x>0)
    #         printf("ABCD");
    #         else 
    #         printf("GH");
    #     }
    #     int main()
    #     {
    #         break;
    #         return;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('a'),[VarDecl('x',FloatType())],VoidType(),Block([If(BinaryOp('>',Id('x'),IntLiteral(0)),CallExpr(Id('printf'),[StringLiteral('ABCD')]),CallExpr(Id('printf'),[StringLiteral('GH')]))])),FuncDecl(Id('main'),[],IntType(),Block([Break(),Return()]))]) )
    #     self.assertTrue(TestAST.checkASTGen(input,expect,350))
    # def test_AST_51(self):
    #     input = """int main()
    #     {
    #         // cho HCN co chieu dai a, chieu rong b
    #         int a,b;
    #         a=100;
    #         b=500;
    #         //chu vi hinh chu nhat
    #         C=2*(a+b);
    #         //dien tich hinh chu nhat
    #         S=a*b;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',IntType()),VarDecl('b',IntType()),BinaryOp('=',Id('a'),IntLiteral(100)),BinaryOp('=',Id('b'),IntLiteral(500)),BinaryOp('=',Id('C'),BinaryOp('*',IntLiteral(2),BinaryOp('+',Id('a'),Id('b')))),BinaryOp('=',Id('S'),BinaryOp('*',Id('a'),Id('b')))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,351))
    # def test_AST_52(self):
    #     input = """int main()
    #     {
    #         float x,y;
    #         x=3.14;
    #         321=_[123]+_[324]-_abcd;
    #         array[test(2)] == b;
    #     }
    #     """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('x',FloatType()),VarDecl('y',FloatType()),BinaryOp('=',Id('x'),FloatLiteral(3.14)),BinaryOp('=',IntLiteral(321),BinaryOp('-',BinaryOp('+',ArrayCell(Id('_'),IntLiteral(123)),ArrayCell(Id('_'),IntLiteral(324))),Id('_abcd'))),BinaryOp('==',ArrayCell(Id('array'),CallExpr(Id('test'),[IntLiteral(2)])),Id('b'))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,352))
    # def test_AST_53(self):
    #     input = """void max(int a,int b)
    #     {
    #         if(a>b)
    #         return b;
    #         else 
    #         return a;
    #     }
    #     int main()
    #     {
    #         max(6,9);
    #         max(b-a,c);
    #         if(a>b)
    #             countinue;
    #             else 
    #             break;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('max'),[VarDecl('a',IntType()),VarDecl('b',IntType())],VoidType(),Block([If(BinaryOp('>',Id('a'),Id('b')),Return(Id('b')),Return(Id('a')))])),FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('max'),[IntLiteral(6),IntLiteral(9)]),CallExpr(Id('max'),[BinaryOp('-',Id('b'),Id('a')),Id('c')]),If(BinaryOp('>',Id('a'),Id('b')),Id('countinue'),Break())]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,353))
    # def test_AST_54(self):
    #     input = """int main()
    #     {
    #         int i;
    #          for(i;i<=5;i=i+1)
    #          {

    #          }
    #          {

    #          }
    #          {

    #          }
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('i',IntType()),For(Id('i'),BinaryOp('<=',Id('i'),IntLiteral(5)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([])),Block([]),Block([])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,354))
    # def test_AST_55(self):
    #     input = """void prime(int n)
    #     {
    #         int i;
    #         for(i;i<n;i=i+1)
    #         {
    #             if(n%i==0)

    #             return 0;
    #         }
    #         return 1;
    #     }
    #     int main()
    #     {
    #         int k;
    #         // In ra day so nguyen to be hon 100
    #         for(k;k<=100;k=k+1)
    #             if(prime(k)==1)
    #             printf(k);
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('prime'),[VarDecl('n',IntType())],VoidType(),Block([VarDecl('i',IntType()),For(Id('i'),BinaryOp('<',Id('i'),Id('n')),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([If(BinaryOp('==',BinaryOp('%',Id('n'),Id('i')),IntLiteral(0)),Return(IntLiteral(0)))])),Return(IntLiteral(1))])),FuncDecl(Id('main'),[],IntType(),Block([VarDecl('k',IntType()),For(Id('k'),BinaryOp('<=',Id('k'),IntLiteral(100)),BinaryOp('=',Id('k'),BinaryOp('+',Id('k'),IntLiteral(1))),If(BinaryOp('==',CallExpr(Id('prime'),[Id('k')]),IntLiteral(1)),CallExpr(Id('printf'),[Id('k')])))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,355))
    # def test_AST_56(self):
    #     input = """int main()
    #     {
    #         float arr[100];
    #         arr[0] = 100.1;
    #         foo(2)[10];
    #         arr[1] = 200.2;
    #         if(!check)
    #             printf("successful");
    #         return;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('arr',ArrayType(100,FloatType())),BinaryOp('=',ArrayCell(Id('arr'),IntLiteral(0)),FloatLiteral(100.1)),ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),IntLiteral(10)),BinaryOp('=',ArrayCell(Id('arr'),IntLiteral(1)),FloatLiteral(200.2)),If(UnaryOp('!',Id('check')),CallExpr(Id('printf'),[StringLiteral('successful')])),Return()]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,356))
    # def test_AST_57(self):
    #     input = """int main()
    #     {
    #         test(10)*prime(20);
    #         boolean c;
    #         int i;
    #         i=a+3;
    #         if(i>0)
    #         {
    #             int d;
    #             d=d+3;
    #             putInt(3);
    #         }
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('*',CallExpr(Id('test'),[IntLiteral(10)]),CallExpr(Id('prime'),[IntLiteral(20)])),VarDecl('c',BoolType()),VarDecl('i',IntType()),BinaryOp('=',Id('i'),BinaryOp('+',Id('a'),IntLiteral(3))),If(BinaryOp('>',Id('i'),IntLiteral(0)),Block([VarDecl('d',IntType()),BinaryOp('=',Id('d'),BinaryOp('+',Id('d'),IntLiteral(3))),CallExpr(Id('putInt'),[IntLiteral(3)])]))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,357))
    # def test_AST_58(self):
    #     input = """int main()
    #     {
    #         putInt(main);
    #         {
    #             int i;
    #             int main;
    #             main = f= i = 200;
    #             putInt(i);
    #             putInt(main);
    #         }
    #         putInt(main);
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('putInt'),[Id('main')]),Block([VarDecl('i',IntType()),VarDecl('main',IntType()),BinaryOp('=',Id('main'),BinaryOp('=',Id('f'),BinaryOp('=',Id('i'),IntLiteral(200)))),CallExpr(Id('putInt'),[Id('i')]),CallExpr(Id('putInt'),[Id('main')])]),CallExpr(Id('putInt'),[Id('main')])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,358))
    # def test_AST_59(self):
    #     input = """int main()
    #     {
    #         if(!test)
    #         {
    #             break;
    #         }
    #         else 
    #         {
    #             return;
    #         }
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(UnaryOp('!',Id('test')),Block([Break()]),Block([Return()]))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,359))
    # def test_AST_60(self):
    #     input = """int main()
    #     {
    #         if(a<5 || b>100)
    #         {
    #             continue;
    #         }
    #         else
    #         {
    #             do{

    #             }
    #             while a;
    #         }
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('||',BinaryOp('<',Id('a'),IntLiteral(5)),BinaryOp('>',Id('b'),IntLiteral(100))),Block([Continue()]),Block([Dowhile([Block([])],Id('a'))]))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,360))
    # def test_AST_61(self):
    #     input = """int main()
    #     {
    #        int k;
    #        k=100+20000000+999999999;
    #        float t;
    #        t=1.2 + 2.3;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('k',IntType()),BinaryOp('=',Id('k'),BinaryOp('+',BinaryOp('+',IntLiteral(100),IntLiteral(20000000)),IntLiteral(999999999))),VarDecl('t',FloatType()),BinaryOp('=',Id('t'),BinaryOp('+',FloatLiteral(1.2),FloatLiteral(2.3)))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,361))
    # def test_AST_62(self):
    #     input = """int main()
    #     {
    #         /* abcdef*/
    #         printf("ABCDEF");
    #         if(a>b)
    #             a=b;
    #         else
    #         {
    #             return;
    #         }
    #         {

    #         }
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('printf'),[StringLiteral('ABCDEF')]),If(BinaryOp('>',Id('a'),Id('b')),BinaryOp('=',Id('a'),Id('b')),Block([Return()])),Block([])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,362))
    # def test_AST_63(self):
    #     input = """int main()
    #     {
    #         float i,j,k;
    #         i=j=k= 1000.2;
    #         system("pause");
    #         int sum;
    #         int i;
    #         for(i;i<100;i=i+1)
    #         {
    #             sum=sum+i;
    #         }
    #         return sum;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('i',FloatType()),VarDecl('j',FloatType()),VarDecl('k',FloatType()),BinaryOp('=',Id('i'),BinaryOp('=',Id('j'),BinaryOp('=',Id('k'),FloatLiteral(1000.2)))),CallExpr(Id('system'),[StringLiteral('pause')]),VarDecl('sum',IntType()),VarDecl('i',IntType()),For(Id('i'),BinaryOp('<',Id('i'),IntLiteral(100)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([BinaryOp('=',Id('sum'),BinaryOp('+',Id('sum'),Id('i')))])),Return(Id('sum'))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,363))
    # def test_AST_64(self):
    #     input = """float test(int a,float b){
    #         int a,b;
    #         c=10;
    #         {
    #             int d[5];
    #         }
    #         {
    #             do 
    #                 if (a=10) {
    #                     if (a==2) {
    #                         for (x;k;z) {
    #                             for(a;b;c){
    #                                 for (t;x;y) {
    #                                     break;
    #                                 }
    #                             }
    #                         }
    #                     }
    #                 } else break;
    #                 a=a-1;
    #              while a>0;
    #         }
    #         }
    #                 """
    #     expect = str(Program([FuncDecl(Id('test'),[VarDecl('a',IntType()),VarDecl('b',FloatType())],FloatType(),Block([VarDecl('a',IntType()),VarDecl('b',IntType()),BinaryOp('=',Id('c'),IntLiteral(10)),Block([VarDecl('d',ArrayType(5,IntType()))]),Block([Dowhile([If(BinaryOp('=',Id('a'),IntLiteral(10)),Block([If(BinaryOp('==',Id('a'),IntLiteral(2)),Block([For(Id('x'),Id('k'),Id('z'),Block([For(Id('a'),Id('b'),Id('c'),Block([For(Id('t'),Id('x'),Id('y'),Block([Break()]))]))]))]))]),Break()),BinaryOp('=',Id('a'),BinaryOp('-',Id('a'),IntLiteral(1)))],BinaryOp('>',Id('a'),IntLiteral(0)))])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,364))
    # def test_AST_65(self):
    #     input = """void func() {
    #         a = ((((((((b))))))));
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('func'),[],VoidType(),Block([BinaryOp('=',Id('a'),Id('b'))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,365))
    # def test_AST_66(self):
    #     input = """void main(){
    #     do {} {} {} {} {} {}{}{}{}{}{}{}{{}{}{}{}{}{{}{}{}{}{}{}{}}}
    #     {} 
    #     while a <b ;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([Dowhile([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([Block([]),Block([]),Block([]),Block([]),Block([]),Block([]),Block([])])]),Block([])],BinaryOp('<',Id('a'),Id('b')))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,366))
    # def test_AST_67(self):
    #     input = """void main(){
    #         if ( a && c)
    #             if( a <= b )
    #                 a = b ;
    #         else
    #             a && b ;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([If(BinaryOp('&&',Id('a'),Id('c')),If(BinaryOp('<=',Id('a'),Id('b')),BinaryOp('=',Id('a'),Id('b')),BinaryOp('&&',Id('a'),Id('b'))))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,367))
    # def test_AST_68(self):
    #     input = """int main(){
    #         if (a<b)
    #             if(c<d)
    #                 if(d<e)
    #                     return;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('<',Id('a'),Id('b')),If(BinaryOp('<',Id('c'),Id('d')),If(BinaryOp('<',Id('d'),Id('e')),Return())))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,368))
    # def test_AST_69(self):
    #     input = """void main(){
    #         if (a<b)
    #             for(x;y;z)
    #                 do{
    #                     break;
    #                 }
    #                 while c != 0 ;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([If(BinaryOp('<',Id('a'),Id('b')),For(Id('x'),Id('y'),Id('z'),Dowhile([Block([Break()])],BinaryOp('!=',Id('c'),IntLiteral(0)))))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,369))
    # def test_AST_70(self):
    #     input = """void test(int a, int b){
    #         if (a<b)
    #             print("a");
    #         else 
    #             print("b");
    #     }
    #         int main()
    #         {
    #             test(5,10);
    #             continue;
    #             return 0;
    #         }
    #                 """
    #     expect = str(Program([FuncDecl(Id('test'),[VarDecl('a',IntType()),VarDecl('b',IntType())],VoidType(),Block([If(BinaryOp('<',Id('a'),Id('b')),CallExpr(Id('print'),[StringLiteral('a')]),CallExpr(Id('print'),[StringLiteral('b')]))])),FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('test'),[IntLiteral(5),IntLiteral(10)]),Continue(),Return(IntLiteral(0))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,370))
    # def test_AST_71(self):
    #     input = """
    #                void foo ( float a [ ] ) {}
    #             void goo ( float x [ ] ) {
    #             float y [ 10 ] ;
    #             int z [ 10 ] ;
    #             foo ( x ) ; //CORRECT
    #             foo ( y ) ; //CORRECT
    #             foo ( z ) ; //WRONG
    #             } """
    #     expect = str(Program([FuncDecl(Id('foo'),[VarDecl('a',ArrayPointerType(FloatType()))],VoidType(),Block([])),FuncDecl(Id('goo'),[VarDecl('x',ArrayPointerType(FloatType()))],VoidType(),Block([VarDecl('y',ArrayType(10,FloatType())),VarDecl('z',ArrayType(10,IntType())),CallExpr(Id('foo'),[Id('x')]),CallExpr(Id('foo'),[Id('y')]),CallExpr(Id('foo'),[Id('z')])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,371))
    # def test_AST_72(self):
    #     input = """void something(){
    #     d > days_in_month[m]; d = days_in_month[m];
    #     if (is_leap(y)) {
    #     	days_in_month[2] = 29;
    #     }
    #     else {
    #     	days_in_month[2] = 28;
    #     }
    #     day = d;
    #     month = m;
    #     year = y;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('something'),[],VoidType(),Block([BinaryOp('>',Id('d'),ArrayCell(Id('days_in_month'),Id('m'))),BinaryOp('=',Id('d'),ArrayCell(Id('days_in_month'),Id('m'))),If(CallExpr(Id('is_leap'),[Id('y')]),Block([BinaryOp('=',ArrayCell(Id('days_in_month'),IntLiteral(2)),IntLiteral(29))]),Block([BinaryOp('=',ArrayCell(Id('days_in_month'),IntLiteral(2)),IntLiteral(28))])),BinaryOp('=',Id('day'),Id('d')),BinaryOp('=',Id('month'),Id('m')),BinaryOp('=',Id('year'),Id('y'))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,372))
    # def test_AST_73(self):
    #     input = """int main(){
    #         int n;
    #         float Sum;
    #          Sum = 0;
    #         for(i = 0; i < n; i=i+1){
    #             Sum = Sum + 1/n;
    #         }
    #         do
    #         {

    #         }
    #         while a<5;
    #         }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('n',IntType()),VarDecl('Sum',FloatType()),BinaryOp('=',Id('Sum'),IntLiteral(0)),For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),Id('n')),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([BinaryOp('=',Id('Sum'),BinaryOp('+',Id('Sum'),BinaryOp('/',IntLiteral(1),Id('n'))))])),Dowhile([Block([])],BinaryOp('<',Id('a'),IntLiteral(5)))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,373))
    # def test_AST_74(self):
    #     input = """void main(){
    #        int a,b,c;
    #        a=b=c=1;
    #        float f[6];
    #        if (a==b) f[0]=1;
    #        float f;
    #        boolean check;
    #        string t;
    #     }   
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',IntType()),BinaryOp('=',Id('a'),BinaryOp('=',Id('b'),BinaryOp('=',Id('c'),IntLiteral(1)))),VarDecl('f',ArrayType(6,FloatType())),If(BinaryOp('==',Id('a'),Id('b')),BinaryOp('=',ArrayCell(Id('f'),IntLiteral(0)),IntLiteral(1))),VarDecl('f',FloatType()),VarDecl('check',BoolType()),VarDecl('t',StringType())]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,374))
    # def test_AST_75(self):
    #     input = """boolean check_key(string key){
    #                 if(a_in_b(key,TextDecode)==true){
    #                     println("%s is in the word!",key);
    #                 }
    #                 else if(a_in_b(key,TextOriginal)==true){
    #                             println("%s has been guessed before!",key);
    #                         }
    #                         else{
    #                                 println("%s is NOT in the word!",key);
    #                         }
    #             }
    #                 """
    #     expect = str(Program([FuncDecl(Id('check_key'),[VarDecl('key',StringType())],BoolType(),Block([If(BinaryOp('==',CallExpr(Id('a_in_b'),[Id('key'),Id('TextDecode')]),BooleanLiteral(True)),Block([CallExpr(Id('println'),[StringLiteral('%s is in the word!'),Id('key')])]),If(BinaryOp('==',CallExpr(Id('a_in_b'),[Id('key'),Id('TextOriginal')]),BooleanLiteral(True)),Block([CallExpr(Id('println'),[StringLiteral('%s has been guessed before!'),Id('key')])]),Block([CallExpr(Id('println'),[StringLiteral('%s is NOT in the word!'),Id('key')])])))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,375))
    # def test_AST_76(self):
    #     input = """float ran(){
    #             float val;
    #             val=Tofloat(rand())/RAND_MAX;
    #             return val*0.5;
    #         }
    #         float ran_a_b(int a,int b){
    #             float val;
    #             val=a+Tofloat(rand())/RAND_MAX;
    #             return val;
    #         }
    #         float pi(int N){
    #             srand(time(NULL));
    #             int i,j;
    #             j=0;
    #             float x,y;
    #             for(i=0;i<N;i=i+1){
    #                 x=ran();
    #                 y=ran();
    #                 if (x*x+y*y<=0.25) j=j+1;
    #             }
    #             return 4.0*j/N;
    #         }
    #                 """
    #     expect = str(Program([FuncDecl(Id('ran'),[],FloatType(),Block([VarDecl('val',FloatType()),BinaryOp('=',Id('val'),BinaryOp('/',CallExpr(Id('Tofloat'),[CallExpr(Id('rand'),[])]),Id('RAND_MAX'))),Return(BinaryOp('*',Id('val'),FloatLiteral(0.5)))])),FuncDecl(Id('ran_a_b'),[VarDecl('a',IntType()),VarDecl('b',IntType())],FloatType(),Block([VarDecl('val',FloatType()),BinaryOp('=',Id('val'),BinaryOp('+',Id('a'),BinaryOp('/',CallExpr(Id('Tofloat'),[CallExpr(Id('rand'),[])]),Id('RAND_MAX')))),Return(Id('val'))])),FuncDecl(Id('pi'),[VarDecl('N',IntType())],FloatType(),Block([CallExpr(Id('srand'),[CallExpr(Id('time'),[Id('NULL')])]),VarDecl('i',IntType()),VarDecl('j',IntType()),BinaryOp('=',Id('j'),IntLiteral(0)),VarDecl('x',FloatType()),VarDecl('y',FloatType()),For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),Id('N')),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([BinaryOp('=',Id('x'),CallExpr(Id('ran'),[])),BinaryOp('=',Id('y'),CallExpr(Id('ran'),[])),If(BinaryOp('<=',BinaryOp('+',BinaryOp('*',Id('x'),Id('x')),BinaryOp('*',Id('y'),Id('y'))),FloatLiteral(0.25)),BinaryOp('=',Id('j'),BinaryOp('+',Id('j'),IntLiteral(1))))])),Return(BinaryOp('/',BinaryOp('*',FloatLiteral(4.0),Id('j')),Id('N')))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,376))
    # def test_AST_77(self):
    #     input = """int main(){
    #         if (a<b)
    #             return a;
    #         else 
    #             return b;
    #         for (x;y;z)
    #             return a;
    #         do
    #         {
    #             for (a;b;c)
    #                 {   if(1>2)
    #                     break;
    #                     }
    #         }
    #         while a;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(BinaryOp('<',Id('a'),Id('b')),Return(Id('a')),Return(Id('b'))),For(Id('x'),Id('y'),Id('z'),Return(Id('a'))),Dowhile([Block([For(Id('a'),Id('b'),Id('c'),Block([If(BinaryOp('>',IntLiteral(1),IntLiteral(2)),Break())]))])],Id('a'))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,377))
    # def test_AST_78(self):
    #     input = """int main(){
    #         for (i = 0; i < 10; i = i + 1) {
    #             for (j = 10; j >= 0; j = j - 1) {
    #                 if (i == j) putIntLn("i");
    #             }
    #         }
    #     }    
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<',Id('i'),IntLiteral(10)),BinaryOp('=',Id('i'),BinaryOp('+',Id('i'),IntLiteral(1))),Block([For(BinaryOp('=',Id('j'),IntLiteral(10)),BinaryOp('>=',Id('j'),IntLiteral(0)),BinaryOp('=',Id('j'),BinaryOp('-',Id('j'),IntLiteral(1))),Block([If(BinaryOp('==',Id('i'),Id('j')),CallExpr(Id('putIntLn'),[StringLiteral('i')]))]))]))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,378))
    # def test_AST_79(self):
    #     input = """int main(){
    #     if (a)
    #         if(b)
    #             if(c)
    #                 if(d)
    #                     return a;
    #             else return b;
    #                 } """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([If(Id('a'),If(Id('b'),If(Id('c'),If(Id('d'),Return(Id('a')),Return(Id('b'))))))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,379))
    # def test_AST_80(self):
    #     input = """ int main()
    #     {
    #         float a,b,c,d;
    #         printf("Nhap vao 3 so a, b, c: ");
    #         scanf("%f%f%f",a,b,c);
    #         if(a==0)
    #         {
    #             if(b==0)
    #                 {
    #                     if(c==0)
    #                         printf("Phuong trinh co vo so nghiem!");
    #                     else
    #                         printf("Phuong trinh vo nghiem!");
    #                 }
    #             else
    #                 printf("Phuong trinh co nghiem duy nhat la: %f",-c/b);
    #         }
    #         else
    #         {
    #             d=b*b-4*a*c;
    #             if (d<0)
    #                 printf("Phuong trinh vo nghiem!!!");
    #             else if (d==0)
    #                 printf("Phuong trinh co nghiem kep la: %f",-b/(2*a));
    #             else
    #                 printf("Phuong trinh co 2 nghiem phan biet la: %f,%f",(-b+sqrt(d))/(2*a),(-b-sqrt(d))/(2*a));    
    #         }    
        
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('a',FloatType()),VarDecl('b',FloatType()),VarDecl('c',FloatType()),VarDecl('d',FloatType()),CallExpr(Id('printf'),[StringLiteral('Nhap vao 3 so a, b, c: ')]),CallExpr(Id('scanf'),[StringLiteral('%f%f%f'),Id('a'),Id('b'),Id('c')]),If(BinaryOp('==',Id('a'),IntLiteral(0)),Block([If(BinaryOp('==',Id('b'),IntLiteral(0)),Block([If(BinaryOp('==',Id('c'),IntLiteral(0)),CallExpr(Id('printf'),[StringLiteral('Phuong trinh co vo so nghiem!')]),CallExpr(Id('printf'),[StringLiteral('Phuong trinh vo nghiem!')]))]),CallExpr(Id('printf'),[StringLiteral('Phuong trinh co nghiem duy nhat la: %f'),BinaryOp('/',UnaryOp('-',Id('c')),Id('b'))]))]),Block([BinaryOp('=',Id('d'),BinaryOp('-',BinaryOp('*',Id('b'),Id('b')),BinaryOp('*',BinaryOp('*',IntLiteral(4),Id('a')),Id('c')))),If(BinaryOp('<',Id('d'),IntLiteral(0)),CallExpr(Id('printf'),[StringLiteral('Phuong trinh vo nghiem!!!')]),If(BinaryOp('==',Id('d'),IntLiteral(0)),CallExpr(Id('printf'),[StringLiteral('Phuong trinh co nghiem kep la: %f'),BinaryOp('/',UnaryOp('-',Id('b')),BinaryOp('*',IntLiteral(2),Id('a')))]),CallExpr(Id('printf'),[StringLiteral('Phuong trinh co 2 nghiem phan biet la: %f,%f'),BinaryOp('/',BinaryOp('+',UnaryOp('-',Id('b')),CallExpr(Id('sqrt'),[Id('d')])),BinaryOp('*',IntLiteral(2),Id('a'))),BinaryOp('/',BinaryOp('-',UnaryOp('-',Id('b')),CallExpr(Id('sqrt'),[Id('d')])),BinaryOp('*',IntLiteral(2),Id('a')))])))]))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,380))
    # def test_AST_81(self):
    #     input = """int main() {
    #         int array[10];
    #         int sum, loop;
    #         sum = 0;        
    #         printf("Chuong trinh tinh tong gia tri cac phan tu mang: \\n\\n");
    #         for(loop = 9; loop >= 0; loop = loop - 1) {
    #             sum = sum + array[loop];      
    #         }
    #         printf("Tong gia tri cua mang la: %d.", sum);
    #         return 0;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([VarDecl("array",ArrayType(10,IntType())),VarDecl("sum",IntType()),VarDecl("loop",IntType()),BinaryOp("=",Id("sum"),IntLiteral(0)),CallExpr(Id("printf"),[StringLiteral("Chuong trinh tinh tong gia tri cac phan tu mang: \\n\\n")]),For(BinaryOp("=",Id("loop"),IntLiteral(9)),BinaryOp(">=",Id("loop"),IntLiteral(0)),BinaryOp("=",Id("loop"),BinaryOp("-",Id("loop"),IntLiteral(1))),Block([BinaryOp("=",Id("sum"),BinaryOp("+",Id("sum"),ArrayCell(Id("array"),Id("loop"))))])),CallExpr(Id("printf"),[StringLiteral("Tong gia tri cua mang la: %d."),Id("sum")]),Return(IntLiteral(0))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,381))
    # def test_AST_82(self):
    #     input = """int main(){
    #         a() = b() + c() - d()+e()*f(10);
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',CallExpr(Id('a'),[]),BinaryOp('+',BinaryOp('-',BinaryOp('+',CallExpr(Id('b'),[]),CallExpr(Id('c'),[])),CallExpr(Id('d'),[])),BinaryOp('*',CallExpr(Id('e'),[]),CallExpr(Id('f'),[IntLiteral(10)]))))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,382))
    # def test_AST_83(self):
    #     input = """void main(){
    #         int a[5];
    #         a[0]=1;
    #         a[1]=2;
    #         a[2]=3;
    #         a[3]=4;
    #         a[4]=5;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([VarDecl('a',ArrayType(5,IntType())),BinaryOp('=',ArrayCell(Id('a'),IntLiteral(0)),IntLiteral(1)),BinaryOp('=',ArrayCell(Id('a'),IntLiteral(1)),IntLiteral(2)),BinaryOp('=',ArrayCell(Id('a'),IntLiteral(2)),IntLiteral(3)),BinaryOp('=',ArrayCell(Id('a'),IntLiteral(3)),IntLiteral(4)),BinaryOp('=',ArrayCell(Id('a'),IntLiteral(4)),IntLiteral(5))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,383))
    # def test_AST_84(self):
    #     input = """int main(){
    #         test(100)[5/2]=6;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',ArrayCell(CallExpr(Id('test'),[IntLiteral(100)]),BinaryOp('/',IntLiteral(5),IntLiteral(2))),IntLiteral(6))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,384))
    # def test_AST_85(self):
    #     input = """int a,c,d;
    #     void main(){
    #         a=5;
    #         b=4;
    #         c=1;
    #         float str;
    #         str = " I CAN FLY";

    #     }
    #                 """
    #     expect = str(Program([VarDecl('a',IntType()),VarDecl('c',IntType()),VarDecl('d',IntType()),FuncDecl(Id('main'),[],VoidType(),Block([BinaryOp('=',Id('a'),IntLiteral(5)),BinaryOp('=',Id('b'),IntLiteral(4)),BinaryOp('=',Id('c'),IntLiteral(1)),VarDecl('str',FloatType()),BinaryOp('=',Id('str'),StringLiteral(' I CAN FLY'))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,385))
    # def test_AST_86(self):
    #     input = """int main(){
    #         boolean check;
    #         check = true;
    #         if(!check) print(check);
    #         else {
    #             print(!check);
    #         }                  
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('check',BoolType()),BinaryOp('=',Id('check'),BooleanLiteral(True)),If(UnaryOp('!',Id('check')),CallExpr(Id('print'),[Id('check')]),Block([CallExpr(Id('print'),[UnaryOp('!',Id('check'))])]))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,386))
    # def test_AST_87(self):
    #     input = """int main(){
    #         a / 5 + 10 -2 = b * c + e -f %5;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',BinaryOp('-',BinaryOp('+',BinaryOp('/',Id('a'),IntLiteral(5)),IntLiteral(10)),IntLiteral(2)),BinaryOp('-',BinaryOp('+',BinaryOp('*',Id('b'),Id('c')),Id('e')),BinaryOp('%',Id('f'),IntLiteral(5))))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,387))
    # def test_AST_88(self):
    #     input = """int main(){
    #         a[0]=a[1]*a[2]/a[3]+a[4]-a[5]+ 10 / 5*2%100;
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([BinaryOp('=',ArrayCell(Id('a'),IntLiteral(0)),BinaryOp('+',BinaryOp('-',BinaryOp('+',BinaryOp('/',BinaryOp('*',ArrayCell(Id('a'),IntLiteral(1)),ArrayCell(Id('a'),IntLiteral(2))),ArrayCell(Id('a'),IntLiteral(3))),ArrayCell(Id('a'),IntLiteral(4))),ArrayCell(Id('a'),IntLiteral(5))),BinaryOp('%',BinaryOp('*',BinaryOp('/',IntLiteral(10),IntLiteral(5)),IntLiteral(2)),IntLiteral(100))))]))]))
    # #     self.assertTrue(TestAST.checkASTGen(input,expect,388))
    # def test_AST_89(self):
    #     input = """void main(){
    #         printf("Mang du lieu dau vao: ");
    #         display();
    #         printline(50);
    #         quickSort(0,MAX-1);
    #         printf("Mang sau khi da sap xep: ");
    #         display();
    #         printline(50);
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([CallExpr(Id('printf'),[StringLiteral('Mang du lieu dau vao: ')]),CallExpr(Id('display'),[]),CallExpr(Id('printline'),[IntLiteral(50)]),CallExpr(Id('quickSort'),[IntLiteral(0),BinaryOp('-',Id('MAX'),IntLiteral(1))]),CallExpr(Id('printf'),[StringLiteral('Mang sau khi da sap xep: ')]),CallExpr(Id('display'),[]),CallExpr(Id('printline'),[IntLiteral(50)])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,389))
    # def test_AST_90(self):
    #     input = """int main(){
    #         main2(5);
    #         main3(5.5);
    #     }
    #         void main2(){}
    #         string main3(){}
    #         boolean main4(){}
    #         float _(){}
            
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('main2'),[IntLiteral(5)]),CallExpr(Id('main3'),[FloatLiteral(5.5)])])),FuncDecl(Id('main2'),[],VoidType(),Block([])),FuncDecl(Id('main3'),[],StringType(),Block([])),FuncDecl(Id('main4'),[],BoolType(),Block([])),FuncDecl(Id('_'),[],FloatType(),Block([]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,390))
    # def test_AST_91(self):
    #     input = """float minimum(float a, float b, float c)
    #         {
    #             if (a < b)
    #             {
    #                 if (a < c) return a;
    #                 else return c;
    #             }
    #             else {
    #                 if (b < c) return b;
    #                 else return c;
    #             }
    #         }
    #                 """
    #     expect = str(Program([FuncDecl(Id('minimum'),[VarDecl('a',FloatType()),VarDecl('b',FloatType()),VarDecl('c',FloatType())],FloatType(),Block([If(BinaryOp('<',Id('a'),Id('b')),Block([If(BinaryOp('<',Id('a'),Id('c')),Return(Id('a')),Return(Id('c')))]),Block([If(BinaryOp('<',Id('b'),Id('c')),Return(Id('b')),Return(Id('c')))]))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,391))
    # def test_AST_92(self):
    #     input = """float maximum(float a, float b, float c)
    #         {
    #             if (a > b)
    #             {
    #                 if (a > c) return a;
    #                 else return c;
    #             }
    #             else {
    #                 if (b > c) return b;
    #                 else return c;
    #             }
    #         }
    #                 """
    #     expect = str(Program([FuncDecl(Id('maximum'),[VarDecl('a',FloatType()),VarDecl('b',FloatType()),VarDecl('c',FloatType())],FloatType(),Block([If(BinaryOp('>',Id('a'),Id('b')),Block([If(BinaryOp('>',Id('a'),Id('c')),Return(Id('a')),Return(Id('c')))]),Block([If(BinaryOp('>',Id('b'),Id('c')),Return(Id('b')),Return(Id('c')))]))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,392))
    # def test_AST_93(self):
    #     input = """int main()
    #         {
    #             float x, a[10], y1;
    #             int deg, i;

    #             printf("Enter the degree of polynomial equation: ");
    #             scanf("%d", deg);

    #             printf("Ehter the value of x for which the equation is to be evaluated: ");
    #             scanf("%f", x);

    #             for(i=0; i<=deg; i+1)
    #             {
    #                 printf("Enter the coefficient of x to the power %d: ",i);
    #                 scanf("%f",a[i]);
    #             }

    #             y1 = poly(a, deg, x);
                
    #             printf("The value of polynomial equation for the value of x = %.2f is: %.2f",x,y1);
                
    #             return 0;
    #         }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('x',FloatType()),VarDecl('a',ArrayType(10,FloatType())),VarDecl('y1',FloatType()),VarDecl('deg',IntType()),VarDecl('i',IntType()),CallExpr(Id('printf'),[StringLiteral('Enter the degree of polynomial equation: ')]),CallExpr(Id('scanf'),[StringLiteral('%d'),Id('deg')]),CallExpr(Id('printf'),[StringLiteral('Ehter the value of x for which the equation is to be evaluated: ')]),CallExpr(Id('scanf'),[StringLiteral('%f'),Id('x')]),For(BinaryOp('=',Id('i'),IntLiteral(0)),BinaryOp('<=',Id('i'),Id('deg')),BinaryOp('+',Id('i'),IntLiteral(1)),Block([CallExpr(Id('printf'),[StringLiteral('Enter the coefficient of x to the power %d: '),Id('i')]),CallExpr(Id('scanf'),[StringLiteral('%f'),ArrayCell(Id('a'),Id('i'))])])),BinaryOp('=',Id('y1'),CallExpr(Id('poly'),[Id('a'),Id('deg'),Id('x')])),CallExpr(Id('printf'),[StringLiteral('The value of polynomial equation for the value of x = %.2f is: %.2f'),Id('x'),Id('y1')]),Return(IntLiteral(0))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,393))
    # def test_AST_94(self):
    #     input = """int main()
    #         {
    #             // fork() creates child process identical to parent
    #             int pid ;
    #             pid = fork();

    #             // if pid is greater than 0 than it is parent process
    #             // if pid is 0 then it is child process
    #             // if pid is -ve , it means fork() failed to create child process

    #             // Parent process
    #             if (pid > 0)
    #                 sleep(20);
    #         }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('pid',IntType()),BinaryOp('=',Id('pid'),CallExpr(Id('fork'),[])),If(BinaryOp('>',Id('pid'),IntLiteral(0)),CallExpr(Id('sleep'),[IntLiteral(20)]))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,394))
    # def test_AST_95(self):
    #     input = """int main()
    #         {
    #             int x;
                
    #             printf("Enter an integer number: ");
    #             scanf("%d",a);
                
    #             if(x==0)
    #                 printf("%d",0);
    #             else if(x%9==0)
    #                 printf("%d",9);
    #             else 
    #                 return;
    #             }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('x',IntType()),CallExpr(Id('printf'),[StringLiteral('Enter an integer number: ')]),CallExpr(Id('scanf'),[StringLiteral('%d'),Id('a')]),If(BinaryOp('==',Id('x'),IntLiteral(0)),CallExpr(Id('printf'),[StringLiteral('%d'),IntLiteral(0)]),If(BinaryOp('==',BinaryOp('%',Id('x'),IntLiteral(9)),IntLiteral(0)),CallExpr(Id('printf'),[StringLiteral('%d'),IntLiteral(9)]),Return()))]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,395))
    # def test_AST_96(self):
    #     input = """int main() {
    #             int num;
    #             printf("\\nNhap so dia:");
    #             scanf("%d", num);

    #             TOH(num - 1, "A", "B", "C");
    #             return (0);
    #         }

    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([VarDecl('num',IntType()),CallExpr(Id('printf'),[StringLiteral('\\nNhap so dia:')]),CallExpr(Id('scanf'),[StringLiteral('%d'),Id('num')]),CallExpr(Id('TOH'),[BinaryOp('-',Id('num'),IntLiteral(1)),StringLiteral('A'),StringLiteral('B'),StringLiteral('C')]),Return(IntLiteral(0))]))]) )
    #     self.assertTrue(TestAST.checkASTGen(input,expect,396))
    # def test_AST_97(self):
    #     input = """void main(){
    #         if(array[0] > array[1]) {
    #                 largest = array[0];
    #                 second  = array[1];
    #             }else {
    #                 largest = array[1];
    #                 second  = array[0];
    #             }

    #             printf("Chuong trinh tim phan tu lon nhat va lon thu hai cua mang:\\n\\n");
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],VoidType(),Block([If(BinaryOp('>',ArrayCell(Id('array'),IntLiteral(0)),ArrayCell(Id('array'),IntLiteral(1))),Block([BinaryOp('=',Id('largest'),ArrayCell(Id('array'),IntLiteral(0))),BinaryOp('=',Id('second'),ArrayCell(Id('array'),IntLiteral(1)))]),Block([BinaryOp('=',Id('largest'),ArrayCell(Id('array'),IntLiteral(1))),BinaryOp('=',Id('second'),ArrayCell(Id('array'),IntLiteral(0)))])),CallExpr(Id('printf'),[StringLiteral('Chuong trinh tim phan tu lon nhat va lon thu hai cua mang:\\n\\n')])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,397))
    # def test_AST_98(self):
    #     input = """int find_max(int a, int b, int c){
    #             int max;
    #             if (a>b)
    #                 if (a>c) max=a;
    #                 else max=c;
                
    #             if (b>a)
    #                 if (b>c) max=b;
    #                 else max=c;

    #             return max;
    #         }
    #         int main()
    #         {
    #             find_max(5,10,15);
    #         }
    #                 """
    #     expect = str(Program([FuncDecl(Id('find_max'),[VarDecl('a',IntType()),VarDecl('b',IntType()),VarDecl('c',IntType())],IntType(),Block([VarDecl('max',IntType()),If(BinaryOp('>',Id('a'),Id('b')),If(BinaryOp('>',Id('a'),Id('c')),BinaryOp('=',Id('max'),Id('a')),BinaryOp('=',Id('max'),Id('c')))),If(BinaryOp('>',Id('b'),Id('a')),If(BinaryOp('>',Id('b'),Id('c')),BinaryOp('=',Id('max'),Id('b')),BinaryOp('=',Id('max'),Id('c')))),Return(Id('max'))])),FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('find_max'),[IntLiteral(5),IntLiteral(10),IntLiteral(15)])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,398))
    # def test_AST_99(self):
    #     input = """int main(){
    #         printf("The last testcase ");
    #     }
    #                 """
    #     expect = str(Program([FuncDecl(Id('main'),[],IntType(),Block([CallExpr(Id('printf'),[StringLiteral('The last testcase ')])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,399))
    