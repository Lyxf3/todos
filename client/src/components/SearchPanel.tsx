import React from "react";
import {FilterItem} from "./FilterItem";
import {SearchItem} from "./SearchItem";
import container from "../styles/containers.module.css"
import {Col, Row} from "antd";

export const SearchPanel: React.FC = () => {
    return (
        <Row className={container.filter}>
            <Col flex={9}>
                <SearchItem />
            </Col>
            <Col flex={1}>
                <FilterItem />
            </Col>
        </Row>
    )
}