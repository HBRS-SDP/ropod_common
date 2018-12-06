#include "ZyreBaseCommunicator.h"
#include <iostream>
#include <sstream>

class CCU : public ZyreBaseCommunicator
{
    public:
    CCU(const std::string &nodeName,
	    const std::vector<std::string> &groups,
	    const std::vector<std::string> &messageTypes,
	    const bool &printAllReceivedMessages)
    : ZyreBaseCommunicator(nodeName, groups, messageTypes, printAllReceivedMessages)
    {};

    private:
    virtual void recvMsgCallback(ZyreMsgContent* msgContent);
    virtual void sendMessageStatusCallback(const std::string &msgId, bool status);
};

void CCU::recvMsgCallback(ZyreMsgContent* msgContent)
{
    //std::cout << this->getNodeName() << " received message" << "\n";
    //std::cout << message << "\n";
}

void CCU::sendMessageStatusCallback(const std::string &msgId, bool status)
{
}

int main(int argc, char *argv[])
{
    std::vector<std::string> groups;
    groups.push_back("Group1");
    groups.push_back("Group2");
    groups.push_back("Group3");

    std::vector<std::string> messageTypes;
    bool b = true;

    {
        CCU CCU_test_1("CCU_test_1", groups, messageTypes, b);
        CCU CCU_test_2("CCU_test_2", groups, messageTypes, b);
        CCU_test_1.printJoinedGroups();
        CCU_test_2.printJoinedGroups();
        zclock_sleep(3000);
    }


    CCU CCU_test_1("CCU_test_1", groups, messageTypes, b);
    CCU CCU_test_2("CCU_test_2", groups, messageTypes, b);

    for (int i = 0; i < 10; i++)
    {
        std::stringstream msg;
        msg << "Hello to all groups NR " << i;
        CCU_test_1.shout(msg.str());
    }
    CCU_test_1.shout("Now only to group 3", "Group3");
    CCU_test_2.leaveGroup("Group2");
    CCU_test_1.shout("Now only to group 2", "Group2");
    CCU_test_2.printJoinedGroups();
    CCU_test_2.joinGroup("Group2");
    CCU_test_2.printJoinedGroups();
    CCU_test_1.shout("Now only to group 2 again", "Group2");

//    std::cout << my_ccu.getZyreParams().groups.size() << std::endl;
//    my_ccu.printJoinedGroups();
//    my_ccu.joinGroup("Group1");
//    my_ccu.printJoinedGroups();

    zclock_sleep(15000);
    return 0;
}
