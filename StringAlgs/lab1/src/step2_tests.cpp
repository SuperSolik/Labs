#include <gtest/gtest.h>
#include "funcs.h"

struct TestItem
{
    const char* str1;
    const char* str2;
	int res;
};

class Test : public ::testing::Test, public ::testing::WithParamInterface<TestItem> {};

TEST_P(Test, circle_test)
{
    TestItem item = GetParam();
    ASSERT_EQ(checkCircle(item.str1, item.str2), item.res);
}

INSTANTIATE_TEST_CASE_P(
        TestInstantiation,
        Test,
        ::testing::Values(
                TestItem {"defabc", "abcdef", 3},
				TestItem {"asdasdsa", "sadasdsads", -1},
				TestItem {"test", "test", 0},
				TestItem {"aaaaaaaaaaabb", "bbaaaaaaaaaaa", 11},
				TestItem {"aaaaccccb", "ccccbaaaa", 4}
));

int main(int argc, char* argv[]){
    testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}
