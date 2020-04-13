class Parents:
    def func(self):
        print("부모클래스 메쏘드 입니다.")


class Child(Parents):
    def func(self):
        print("자식클래스 메쏘드 입니다.")


temp = Child()
temp.func()
""" 메소드 오버라이딩(Overriding):
자식 클래스에서 부모 클래스의 메쏘드를 재정의하는 것을 오버라이딩(Overriding) 이라 한다.
오버라이딩은 무시하다, 우선하다라는 의미를 가지는데, 뜻과 같이 부모클래스의 원래 메쏘드를 무시하고,
자식클래스에서 새로 정의한 메쏘드대로 사용하는 것이다.

이러는 방법은 부모 클래스의 메쏘드 이름과 똑같은 이름으로 자식 클래스에 메쏘드를 만들면 되는데,
프로그램에서 메쏘드 오버라이딩은 어떤기능이 같은 메쏘드이름으로 계속 사용되어야할 때 활용한다.
"""


class Parents:
    def func(self):
        print("부모클래스 메쏘드 입니다.")


class Child(Parents):
    def func(self):
        super().func()
        print("자식클래스 메쏘드 입니다.")


temp = Child()
temp.func()
"""
만약에 부모클래스의 메쏘드를 자식클래스의 메쏘드로 오버라이딩할 때 부모클래스 메쏘드를 재활용 할 수도 있다.
마찬가지로 super().메쏘드 
를 사용해서 부모클래스의 오버라이딩할 메쏘드를 호출하는 것이다.

이런방법처럼 메쏘드 오버라이딩은 원래기능을 유지하면서 새로운 기능을 덧붙일 때 사용할 수 있다.
"""