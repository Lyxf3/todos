import React from 'react';
import {SearchPanel} from "../components/SearchPanel";
import {TodoList} from "../components/TodoList";
import 'antd/dist/antd.css';

import '../styles/App.css';
import { Layout} from 'antd';
const { Header, Content, Footer } = Layout;

function App(): JSX.Element {
  return (
    <Layout className="layout" >
      <Header className="header">
        <div className="logo" />
        <SearchPanel />
      </Header>
      <Content className="content">
        <div className="site-layout-content">
          <TodoList />
        </div>
      </Content>
      <Footer className="footer">
        Dmitriy "LyxF3" Zhyhylii 03.08.2021
      </Footer>
    </Layout>
  )
}

export default App;