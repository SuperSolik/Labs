#include <gtest/gtest.h>
#include "funcs.h"

struct TestItem
{
    const char* pattern;
    const char* text;
	const char* res;
};

class Test : public ::testing::Test, public ::testing::WithParamInterface<TestItem> {};

TEST_P(Test, kmp_test)
{
    TestItem item = GetParam();
    ASSERT_EQ(kmp(item.pattern, item.text), item.res);
}

INSTANTIATE_TEST_CASE_P(
        TestInstantiation,
        Test,
        ::testing::Values(
                TestItem {"a", "aaa", "0,1,2"},
				TestItem {"aaa", "bbb", "-1"},
				TestItem {"test", "test", "0"},
				TestItem {"s", "xzasdsasdcsad", "3,5,7,10"},
				TestItem {"def", "abcdef", "3"}
));

int main(int argc, char* argv[]){
    testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}
