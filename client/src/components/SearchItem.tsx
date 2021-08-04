import React from "react";
import {Input} from "antd";
import {SearchOutlined} from "@ant-design/icons";

export const SearchItem: React.FC = (props) => {
    const {} = props
    return (
        <>
            <Input size="large" placeholder="Search..." prefix={<SearchOutlined />} />
        </>
    )
}