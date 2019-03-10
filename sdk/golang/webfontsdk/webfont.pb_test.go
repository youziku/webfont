package webfontsdk

import (
	"context"
	"log"
	"testing"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/status"
)

func Test_build(t *testing.T) {
	var err error
	var conn *grpc.ClientConn
	conn, err = grpc.Dial("localhost:5000", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := NewGreeterClient(conn)
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	req := &FontBuildRequest{
		FontId:   45803,
		Apikey:   "798e7dac-bdd4-4049-b03c-7cce5832e013",
		Text:     "English 中文字体测试",
		NeedTtf:  true,
		NeedEot:  true,
		NeedWoff: true,
	}
	if ret, err := c.BuildFont(ctx, req); err != nil {
		if actual, ok := status.FromError(err); ok {
			t.Fatal("actual", "code", actual.Code(), "err:", actual.Message())
		}
	} else {
		t.Log("ttf", len(ret.GetBytesTtf()), "eot", len(ret.GetBytesEot()), "woff", len(ret.GetBytesWoff()))
		//拼装font-familly
	}
}

func Test_getlist(t *testing.T) {
	var err error
	var conn *grpc.ClientConn
	conn, err = grpc.Dial("localhost:5000", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := NewGreeterClient(conn)
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	req := &FontListRequet{
		Apikey: "f4e14370-d87f-40b3-a845-be80a75f74f4",
	}
	if ret, err := c.GetFontList(ctx, req); err != nil {
		if actual, ok := status.FromError(err); ok {
			t.Fatal("actual", "code", actual.Code(), "err:", actual.Message())
		}
	} else {
		for k, v := range ret.Fonts {
			t.Log("list", k, v)
		}
		//拼装font-familly
	}
}
