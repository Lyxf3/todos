import React from "react";
import {HeartOutlined, StarOutlined} from "@ant-design/icons";
import container from "../styles/containers.module.css"
import styles from "../styles/elements.module.css"
import {Button} from "antd";

export const FilterItem: React.FC = () => {
  return (
      <div className={container.icons}>
          <Button
              shape="circle"
              icon={<HeartOutlined className={styles.icon}/>}
          />
          <Button
              shape="circle"
              icon={<StarOutlined className={styles.icon}/>}
          />
      </div>
  )
}